# Generated by Django 4.1.7 on 2023-05-06 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0036_alter_transactionrecord_numguests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionrecord',
            name='numguests',
        ),
    ]