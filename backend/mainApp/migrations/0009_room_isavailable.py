# Generated by Django 4.1.7 on 2023-03-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_transactionitem_itemoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
    ]
