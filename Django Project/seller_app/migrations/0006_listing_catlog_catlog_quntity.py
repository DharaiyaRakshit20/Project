# Generated by Django 4.2.2 on 2023-07-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_app', '0005_listing_catlog_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing_catlog',
            name='Catlog_Quntity',
            field=models.CharField(max_length=50, null=True),
        ),
    ]