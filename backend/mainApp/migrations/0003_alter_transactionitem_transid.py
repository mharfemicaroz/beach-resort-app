# Generated by Django 4.1.7 on 2023-04-07 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_transactionitem_transid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionitem',
            name='transid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]