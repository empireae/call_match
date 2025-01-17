# Generated by Django 5.0.6 on 2024-07-03 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletModel',
            fields=[
                ('wallet_id', models.AutoField(primary_key=True, serialize=False)),
                ('wallet_coins', models.IntegerField(default=1000, null=True)),
                ('purchase_date', models.DateField(null=True)),
                ('agent_balance', models.IntegerField(default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.customermodel')),
            ],
        ),
    ]
