# Generated by Django 4.1.7 on 2023-05-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0045_restotables'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestoOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_type', models.CharField(max_length=255)),
                ('table_id', models.IntegerField()),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('items', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
