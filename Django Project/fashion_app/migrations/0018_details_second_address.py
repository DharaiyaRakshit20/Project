# Generated by Django 4.2.2 on 2023-07-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_app', '0017_cart_stetus'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='second_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
