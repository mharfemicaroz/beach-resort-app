# Generated by Django 4.1.7 on 2023-05-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0047_restoorders_processedby_restoorders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='restoitem',
            name='inventory',
            field=models.TextField(blank=True, null=True),
        ),
    ]
