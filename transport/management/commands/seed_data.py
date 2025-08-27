from django.core.management.base import BaseCommand
from transport.models import Vehicle, Driver, Order

class Command(BaseCommand):
    help = "Create sample mockup"

    def handle(self, *args, **options):
        vehicles = [
            {"license_plate": "AA123BT", "vehicle_type": "van",   "max_capacity_kg": 1200, "cost_per_km": 1.0, "pos_x": 5,  "pos_y": 5},
            {"license_plate": "AA456BT", "vehicle_type": "truck", "max_capacity_kg": 8000, "cost_per_km": 1.6, "pos_x": 10, "pos_y": 2},
            {"license_plate": "AA789BT", "vehicle_type": "van",   "max_capacity_kg": 1500, "cost_per_km": 0.9, "pos_x": 18, "pos_y": 20},
            {"license_plate": "AA910BT", "vehicle_type": "truck", "max_capacity_kg": 12000,"cost_per_km": 1.8, "pos_x": 50, "pos_y": 40},
            {"license_plate": "AA999BT", "vehicle_type": "van",   "max_capacity_kg": 900,  "cost_per_km": 0.8, "pos_x": 7,  "pos_y": 9},
        ]
        for v in vehicles:
            Vehicle.objects.get_or_create(license_plate=v["license_plate"], defaults=v)

        drivers = [
            {"name": "Jozef", "phone": "+421900000001", "license_number": "SK001"},
            {"name": "Dusan", "phone": "+421900000002", "license_number": "SK002"},
            {"name": "Pavol", "phone": "+421900000003", "license_number": "SK003"},
        ]
        for d in drivers:
            Driver.objects.get_or_create(license_number=d["license_number"], defaults=d)

        orders = [
            {"order_number": "ORD1001", "customer_name": "SRucenim s.r.o.", "pickup_address": "Ulica jeden", "delivery_address": "Ulica dva", "total_weight_kg": 800,  "pickup_x": 6,  "pickup_y": 6},
            {"order_number": "ORD1002", "customer_name": "Akciova a.s.", "pickup_address": "Ulica tri", "delivery_address": "Ulica 4", "total_weight_kg": 2000, "pickup_x": 15, "pickup_y": 3},
        ]
        for o in orders:
            Order.objects.get_or_create(order_number=o["order_number"], defaults=o)

        self.stdout.write(self.style.SUCCESS("Sample data created."))
