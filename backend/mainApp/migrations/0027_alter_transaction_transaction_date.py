# Generated by Django 4.1.7 on 2023-04-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_alter_transaction_transaction_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
