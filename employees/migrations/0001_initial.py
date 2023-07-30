# Generated by Django 4.2.3 on 2023-07-30 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacation_rate', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
