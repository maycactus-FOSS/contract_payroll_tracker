from django.db import models
from employees.models import Employee

class OperatingExpense(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    federal_tax = models.DecimalField(max_digits=8, decimal_places=2)
    provincial_tax = models.DecimalField(max_digits=8, decimal_places=2)
    cpp = models.DecimalField(max_digits=8, decimal_places=2)
    ei = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Expense for {self.employee} on {self.date}"