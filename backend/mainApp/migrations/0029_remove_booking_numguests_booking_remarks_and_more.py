# Generated by Django 4.1.7 on 2023-04-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0028_customuser_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='numGuests',
        ),
        migrations.AddField(
            model_name='booking',
            name='remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='clientaddress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contactNumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='clientaddress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='clientcontact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
