# Generated by Django 4.2.2 on 2023-07-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_app', '0011_rename_detailss_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
