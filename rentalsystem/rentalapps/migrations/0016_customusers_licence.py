# Generated by Django 5.0 on 2024-02-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapps', '0015_alter_customusers_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='licence',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
