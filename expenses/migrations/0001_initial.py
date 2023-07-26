# Generated by Django 4.2.3 on 2023-07-26 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hours_worked', models.DecimalField(decimal_places=2, max_digits=5)),
                ('federal_tax', models.DecimalField(decimal_places=2, max_digits=8)),
                ('provincial_tax', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cpp', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ei', models.DecimalField(decimal_places=2, max_digits=8)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]