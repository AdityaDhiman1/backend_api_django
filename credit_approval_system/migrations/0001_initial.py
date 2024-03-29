# Generated by Django 4.2.9 on 2024-01-17 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('monthly_income', models.IntegerField(blank=True, default=0, null=True)),
                ('approved_limit', models.IntegerField(blank=True, default=0, null=True)),
                ('current_debt', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.IntegerField(blank=True, null=True)),
                ('loan_amount', models.IntegerField(default=0)),
                ('tenure', models.IntegerField()),
                ('interest_rate', models.FloatField()),
                ('paid_on_time', models.BooleanField(default=False)),
                ('monthly_payment', models.IntegerField()),
                ('emi_paid_on_time', models.IntegerField(default=0)),
                ('date_of_approval', models.DateField()),
                ('end_date', models.DateField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit_approval_system.customer')),
            ],
        ),
    ]
