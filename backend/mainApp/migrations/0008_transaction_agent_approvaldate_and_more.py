# Generated by Django 4.1.7 on 2023-08-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_remove_transaction_cashor_remove_transaction_cashos'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='agent_approvalDate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='agent_isApproved',
            field=models.BooleanField(default=False),
        ),
    ]