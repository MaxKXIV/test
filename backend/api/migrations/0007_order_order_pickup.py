# Generated by Django 4.2.10 on 2024-03-06 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_order_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_pickup',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
