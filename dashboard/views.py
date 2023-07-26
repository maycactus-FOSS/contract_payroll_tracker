# dashboard/views.py
from django.shortcuts import render, get_object_or_404
from contracts.models import Contract
from employees.models import Employee
from expenses.models import OperatingExpense
from datetime import datetime  # Add this import line

def default_dashboard(request):
    return render(request, 'dashboard/default_dashboard.html')

def business_dashboard(request):
    # Assuming you have a date range input on the dashboard to select the desired period
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Add logic here to calculate revenue, expenses, and travel distance for the selected period
    contracts = Contract.objects.filter(date__range=(start_date, end_date))
    revenue = sum(contract.income for contract in contracts)
    expenses = OperatingExpense.objects.filter(date__range=(start_date, end_date))
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
        # Convert the employee_id to an integer (assuming it's a numeric value)
        employee_id = int(employee_id)
    except ValueError:
        # Handle the case when the employee_id is not a valid numeric value
        # For example, redirect to an error page or display an error message
        # In this case, we'll raise a 404 page not found error.
        raise Http404("Invalid employee ID")

    # Get the employee instance based on the provided employee_id or return 404 if not found
    employee = get_object_or_404(Employee, employee_id=employee_id)

    # Assuming you have selected a date range for the dashboard
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')


    # Retrieve the operating expenses for the specific employee and date range
    operating_expenses = OperatingExpense.objects.filter(
        employee=employee,
        date__range=(start_date, end_date)
    )

    # Calculate employee income, net income, and deductions using the Employee model methods
    employee_income = employee.calculate_income(operating_expenses)
    employee_net_income = employee.calculate_net_income(operating_expenses)
    employee_deductions = employee.calculate_deductions(operating_expenses)

    # Pass the calculated values to the template or do whatever you need to do with them
    context = {
        'employee': employee,
        'start_date': start_date,
        'end_date': end_date,
        'employee_income': employee_income,
        'employee_net_income': employee_net_income,
        'employee_deductions': employee_deductions,
    }

    return render(request, 'dashboard/employee_dashboard.html', context)