# Generated by Django 4.1.7 on 2023-08-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isNewMessage',
            field=models.BooleanField(default=False),
        ),
    ]
