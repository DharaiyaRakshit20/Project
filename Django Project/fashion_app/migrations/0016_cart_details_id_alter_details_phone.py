# Generated by Django 4.2.2 on 2023-07-15 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_app', '0015_alter_details_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Details_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fashion_app.details'),
        ),
        migrations.AlterField(
            model_name='details',
            name='phone',
            field=models.CharField(max_length=124),
        ),
    ]