# Generated by Django 4.1.7 on 2023-09-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_rename_status_leisureitem_package_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='agent_approvalDate',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='agent_isApproved',
        ),
        migrations.AddField(
            model_name='transactionrecord',
            name='agent_approvalDate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transactionrecord',
            name='agent_isApproved',
            field=models.BooleanField(default=False),
        ),
    ]