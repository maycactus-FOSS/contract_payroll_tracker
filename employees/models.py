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

    def calculate_income(self, operating_expenses):
        # Assuming you have a method to fetch the hours worked by the employee during the selected period
        hours_worked = self.get_hours_worked(operating_expenses)
        income = hours_worked * self.hourly_rate * (1 + self.vacation_rate)
        return income

    def calculate_federal_tax(self, operating_expenses):
        if operating_expenses:
            total_federal_tax = sum(expense.federal_tax for expense in operating_expenses)
        else:
            total_federal_tax = 0
        return total_federal_tax

    def calculate_provincial_tax(self, operating_expenses):
        if operating_expenses:
            total_provincial_tax = sum(expense.provincial_tax for expense in operating_expenses)
        else:
            total_provincial_tax = 0
        return total_provincial_tax

    def calculate_cpp(self, operating_expenses):
        if operating_expenses:
            total_cpp = sum(expense.cpp for expense in operating_expenses)
        else:
            total_cpp = 0
        return total_cpp

    def calculate_ei(self, operating_expenses):
        if operating_expenses:
            total_ei = sum(expense.ei for expense in operating_expenses)
        else:
            total_ei = 0
        return total_ei

    def calculate_net_income(self, operating_expenses):
        hours_worked = self.get_hours_worked(operating_expenses)
        federal_tax = self.calculate_federal_tax(operating_expenses)
        provincial_tax = self.calculate_provincial_tax(operating_expenses)
        cpp = self.calculate_cpp(operating_expenses)
        ei = self.calculate_ei(operating_expenses)
        net_income = hours_worked * self.hourly_rate * (1 + self.vacation_rate) - federal_tax - provincial_tax - cpp - ei
        return net_income

    def calculate_deductions(self, operating_expenses):
        federal_tax = self.calculate_federal_tax(operating_expenses)
        provincial_tax = self.calculate_provincial_tax(operating_expenses)
        cpp = self.calculate_cpp(operating_expenses)
        ei = self.calculate_ei(operating_expenses)
        deductions = federal_tax + provincial_tax + cpp + ei
        return deductions
