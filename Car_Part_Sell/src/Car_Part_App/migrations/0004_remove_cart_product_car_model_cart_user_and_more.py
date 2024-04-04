# Generated by Django 5.0.2 on 2024-03-18 10:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Part_App', '0003_cart_cart_product_delete_carpartpurchase'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_product',
            name='car_model',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart_product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]