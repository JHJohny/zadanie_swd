from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=16, unique=True)),
                ('vehicle_type', models.CharField(choices=[('van', 'Van'), ('truck', 'Truck')], max_length=10)),
                ('max_capacity_kg', models.PositiveIntegerField()),
                ('cost_per_km', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pos_x', models.FloatField()),
                ('pos_y', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('license_number', models.CharField(max_length=50, unique=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('pickup_address', models.CharField(max_length=200)),
                ('delivery_address', models.CharField(max_length=200)),
                ('total_weight_kg', models.PositiveIntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='new', max_length=20)),
                ('pickup_x', models.FloatField()),
                ('pickup_y', models.FloatField()),
                ('assigned_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='transport.driver')),
                ('assigned_vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='transport.vehicle')),
            ],
        ),
    ]
