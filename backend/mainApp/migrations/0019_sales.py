# Generated by Django 4.1.7 on 2023-04-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0018_inventoryitemrecord_delete_purchasesitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sucustomer_name', models.CharField(max_length=255)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]