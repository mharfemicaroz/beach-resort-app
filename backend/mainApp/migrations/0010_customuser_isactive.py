# Generated by Django 4.1.7 on 2023-03-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_room_isavailable'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
