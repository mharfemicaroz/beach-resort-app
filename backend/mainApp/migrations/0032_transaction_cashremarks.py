# Generated by Django 4.1.7 on 2023-04-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0031_transactionitem_groupkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='cashRemarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]