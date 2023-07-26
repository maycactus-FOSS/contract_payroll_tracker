# dashboard/views.py
from django.shortcuts import render, get_object_or_404
from contracts.models import Contract
from employees.models import Employee
from payrolls.models import PayrollExpense
from functools import lru_cache


def default_dashboard(request):
    return render(request, 'dashboard/default_dashboard.html')


def business_dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    contracts = Contract.objects.filter(date__range=(start_date, end_date))
    revenue = sum(contract.income for contract in contracts)
    expenses = PayrollExpense.objects.filter(date__range=(start_date, end_date))
    total_expenses = sum(expense.total_expense() for expense in expenses)
    travel_distance = sum(contract.travel_distance for contract in contracts)
    net_income = revenue - total_expenses

    return render(request, 'dashboard/business_dashboard.html', {
        'start_date': start_date,
        'end_date': end_date,
        'revenue': revenue,
        'total_expenses': total_expenses,
        'travel_distance': travel_distance,
        'net_income': net_income,
    })


def employee_dashboard(request, employee_id):
    try:
        employee_id = int(employee_id)
    except ValueError:
        raise Http404("Invalid employee ID")

    employee = get_object_or_404(Employee, employee_id=employee_id)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    payroll_expenses = PayrollExpense.objects.filter(
        employee=employee,
        date__range=(start_date, end_date)
    )

    # Calculate employee income, net income, tax, CPP, and EI deductions using the helper functions
    income = calculate_employee_income(employee, payroll_expenses)
    federal_tax = calculate_federal_tax(employee, payroll_expenses)
    provincial_tax = calculate_provincial_tax(employee, payroll_expenses)
    cpp = calculate_cpp(employee, payroll_expenses)
    ei = calculate_ei(employee, payroll_expenses)
    net_income = calculate_employee_net_income(employee, payroll_expenses)

    # Pass the calculated values to the template or do whatever you need to do with them
    context = {
        'employee': employee,
        'start_date': start_date,
        'end_date': end_date,
        'income': income,
        'federal_tax': federal_tax,
        'provincial_tax': provincial_tax,
        'cpp': cpp,
        'ei': ei,
        'net_income': net_income,
    }

    return render(request, 'dashboard/employee_dashboard.html', context)

# Helper functions to calculate employee income, and net income


@lru_cache(maxsize=None)
def calculate_employee_income(employee, payroll_expenses):
    hours_worked = employee.get_hours_worked(payroll_expenses)
    income = hours_worked * employee.hourly_rate * (1 + employee.vacation_rate)
    return income


@lru_cache(maxsize=None)
def calculate_federal_tax(employee, payroll_expenses):
    if payroll_expenses:
        total_federal_tax = sum(
            expense.federal_tax for expense in payroll_expenses)
    else:
        total_federal_tax = 0
    return total_federal_tax


@lru_cache(maxsize=None)
def calculate_provincial_tax(employee, payroll_expenses):
    if payroll_expenses:
        total_provincial_tax = sum(
            expense.provincial_tax for expense in payroll_expenses)
    else:
        total_provincial_tax = 0
    return total_provincial_tax


@lru_cache(maxsize=None)
def calculate_cpp(employee, payroll_expenses):
    if payroll_expenses:
        total_cpp = sum(expense.cpp for expense in payroll_expenses)
    else:
        total_cpp = 0
    return total_cpp


@lru_cache(maxsize=None)
def calculate_ei(employee, payroll_expenses):
    if payroll_expenses:
        total_ei = sum(expense.ei for expense in payroll_expenses)
    else:
        total_ei = 0
    return total_ei


@lru_cache(maxsize=None)
def calculate_employee_net_income(employee, payroll_expenses):
    hours_worked = employee.get_hours_worked(payroll_expenses)
    federal_tax = calculate_federal_tax(employee, payroll_expenses)
    provincial_tax = calculate_provincial_tax(employee, payroll_expenses)
    cpp = calculate_cpp(employee, payroll_expenses)
    ei = calculate_ei(employee, payroll_expenses)
    net_income = hours_worked * employee.hourly_rate * \
        (1 + employee.vacation_rate) - federal_tax - provincial_tax - cpp - ei
    return net_income
