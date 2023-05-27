# Generated by Django 4.1.7 on 2023-05-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0042_restoitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestoTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taxValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discountValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalCharge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalPay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('items', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]