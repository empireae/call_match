# Generated by Django 5.0.6 on 2024-07-25 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0024_alter_customermodel_adhaar_no'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_object_id', models.PositiveIntegerField()),
                ('amount', models.CharField(max_length=100)),
                ('razorpay_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_signature', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('package_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.customermodel')),
            ],
        ),
    ]
