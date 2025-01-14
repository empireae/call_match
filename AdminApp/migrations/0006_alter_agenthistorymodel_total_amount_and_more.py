# Generated by Django 5.0.6 on 2024-07-05 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_rename_user_agenthistorymodel_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenthistorymodel',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agenthistorymodel',
            name='total_minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agenthistorymodel',
            name='withdrawal',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='UserHistoryModel',
            fields=[
                ('userhistory_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_coins', models.IntegerField()),
                ('total_minutes', models.IntegerField()),
                ('last_purchase_date', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.customermodel')),
            ],
        ),
    ]
