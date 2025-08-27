from django.db import models

class Vehicle(models.Model):
    VAN = "van"
    TRUCK = "truck"
    VEHICLE_TYPES = [(VAN, "Van"), (TRUCK, "Truck")]

    license_plate = models.CharField(max_length=16, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    max_capacity_kg = models.PositiveIntegerField()
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    pos_x = models.FloatField(help_text="Current x position on 2D grid")
    pos_y = models.FloatField(help_text="Current y position on 2D grid")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["license_plate"]

    def __str__(self):
        return f"{self.license_plate} ({self.vehicle_type})"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    license_number = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_ASSIGNED = "assigned"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_ASSIGNED, "Assigned"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    pickup_address = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=200)
    pickup_x = models.FloatField(help_text="Pickup x coord on 2D grid for distance calc")
    pickup_y = models.FloatField(help_text="Pickup y coord on 2D grid for distance calc")
    total_weight_kg = models.PositiveIntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)

    assigned_vehicle = models.ForeignKey('Vehicle', null=True, blank=True, on_delete=models.SET_NULL, related_name="orders")
    assigned_driver = models.ForeignKey('Driver', null=True, blank=True, on_delete=models.SET_NULL, related_name="orders")

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return f"Order {self.order_number}"
