# Generated by Django 4.1.4 on 2023-08-25 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='BookingDate',
            new_name='Booking_Date',
        ),
    ]
