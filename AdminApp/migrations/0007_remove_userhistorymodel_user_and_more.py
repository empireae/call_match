# Generated by Django 5.0.6 on 2024-07-05 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0006_alter_agenthistorymodel_total_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhistorymodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='AgentHistoryModel',
        ),
        migrations.DeleteModel(
            name='UserHistoryModel',
        ),
    ]
