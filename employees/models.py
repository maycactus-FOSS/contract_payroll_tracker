from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vacation_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Employee - {self.name}"
