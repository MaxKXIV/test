# Generated by Django 4.2.10 on 2024-03-01 22:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_pass', models.CharField(max_length=20)),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('rest_id', models.AutoField(primary_key=True, serialize=False)),
                ('manager_id', models.CharField(max_length=20)),
                ('manager_pass', models.CharField(max_length=20)),
                ('rest_phone', models.CharField(max_length=20)),
                ('rest_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_status', models.CharField(choices=[('placed', 'Order placed'), ('inProgress', 'Order in progress'), ('pickup', 'Ready for pickup'), ('completed', 'Order completed')], default='placed', max_length=20)),
                ('order_instruction', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=20)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item_desc', models.TextField(blank=True)),
                ('item_availability', models.IntegerField(blank=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant')),
            ],
        ),
    ]
