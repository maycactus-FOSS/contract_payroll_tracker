from django.db import models
from employees.models import Employee

class PayrollExpense(models.Model):
    payroll_id = models.AutoField(primary_key=True)
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    federal_tax = models.DecimalField(max_digits=8, decimal_places=2)
    provincial_tax = models.DecimalField(max_digits=8, decimal_places=2)
    cpp = models.DecimalField(max_digits=8, decimal_places=2)
    ei = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Payroll Expense for {self.employee} on {self.date}"

    def calculate_total_expense(self):
        employee_income = self.hours_worked * self.employee.hourly_rate * (1 + self.employee.vacation_rate)
        employer_cpp_ei_contribution = self.cpp + self.ei
        return employee_income + employer_cpp_ei_contribution
    
    def calculate_total_remittance(self):
        employer_cpp_ei_contribution = self.cpp + self.ei
        return self.federal_tax + self.provincial_tax + 2 * employer_cpp_ei_contribution