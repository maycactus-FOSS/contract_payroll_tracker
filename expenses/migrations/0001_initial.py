# Generated by Django 4.2.3 on 2023-07-30 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=25)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
            ],
        ),
    ]
