# Generated by Django 5.0.2 on 2024-03-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Part_App', '0006_alter_cart_user_alter_cart_product_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
