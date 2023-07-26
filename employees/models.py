# employees/models.py
from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vacation_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Employee - {self.name}"

    def get_hours_worked(self, operating_expenses):
        if operating_expenses:
            hours_worked = sum(expense.hours_worked for expense in operating_expenses)
        else:
            hours_worked = 0
        return hours_worked