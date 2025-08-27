from math import sqrt
from decimal import Decimal, ROUND_HALF_UP
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Vehicle, Driver, Order
from .serializers import VehicleSerializer, DriverSerializer, OrderSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=["post"], url_path="assign-vehicle")
    def assign_vehicle(self, request, pk=None):
        order = self.get_object()

        if order.status not in [Order.STATUS_NEW, Order.STATUS_CANCELLED]:
            return Response(
                {"detail": f"Order is in '{order.status}' status and cannot be changed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # maybe implement some logic based on distance istead of choosing the first one
        vehicle = (
            Vehicle.objects
            .filter(is_available=True, max_capacity_kg__gte=order.total_weight_kg)
            .order_by("id")
            .first()
        )
        if not vehicle:
            return Response(
                {"detail": "No available vehicle with enough capacity."},
                status=status.HTTP_400_BAD_REQUEST
            )

        driver = Driver.objects.filter(is_available=True).order_by("id").first()
        if not driver:
            return Response(
                {"detail": "No driver available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        distance = sqrt((vehicle.pos_x - order.pickup_x) ** 2 + (vehicle.pos_y - order.pickup_y) ** 2)
        estimated_cost = (Decimal(distance) * vehicle.cost_per_km).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        with transaction.atomic():
            v_locked = Vehicle.objects.select_for_update().get(pk=vehicle.pk)
            d_locked = Driver.objects.select_for_update().get(pk=driver.pk)
            o_locked = Order.objects.select_for_update().get(pk=order.pk)

            if not v_locked.is_available or not d_locked.is_available:
                return Response(
                    {"detail": "Selected vehicle/driver is not available. Retry."},
                    status=status.HTTP_409_CONFLICT
                )

            v_locked.is_available = False
            d_locked.is_available = False
            o_locked.assigned_vehicle = v_locked
            o_locked.assigned_driver = d_locked
            o_locked.status = Order.STATUS_ASSIGNED

            v_locked.save()
            d_locked.save()
            o_locked.save()

        return Response(
            {
                "assigned_vehicle": vehicle.license_plate,
                "assigned_driver": driver.name,
                "estimated_cost": float(estimated_cost),
                "distance_km": round(distance, 2),
            },
            status=status.HTTP_200_OK
        )
