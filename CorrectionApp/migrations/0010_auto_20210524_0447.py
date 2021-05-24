# Generated by Django 3.2.3 on 2021-05-24 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CorrectionApp', '0009_auto_20190905_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booking_end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booking_start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]