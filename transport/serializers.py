from rest_framework import serializers
from .models import Vehicle, Driver, Order

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("status", "assigned_vehicle", "assigned_driver", "creation_date")

# Maybe DRY?