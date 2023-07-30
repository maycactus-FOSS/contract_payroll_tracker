# employees/models.py
from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    vacation_rate = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return f"Employee - {self.name}"