# Generated by Django 5.0 on 2024-01-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapps', '0008_booking_rating_booking_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='review',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
