# Generated by Django 4.2.2 on 2023-07-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_app', '0012_cart_product_color_cart_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]
