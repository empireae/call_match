# Generated by Django 5.0.6 on 2024-07-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_first_name', models.CharField(max_length=100)),
                ('customer_last_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_contact', models.CharField(max_length=50)),
                ('customer_password', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Normal User', 'Normal User'), ('Agent User', 'Agent User')], default='Normal User', max_length=20)),
            ],
        ),
    ]
