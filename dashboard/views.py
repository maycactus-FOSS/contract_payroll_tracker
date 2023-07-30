# dashboard/views.py
from django.shortcuts import render, get_object_or_404
from contracts.models import Contract
from employees.models import Employee
from expenses.models import Expense
from payrolls.models import PayrollExpense
from datetime import datetime, date


def home(request):
    return render(request, 'dashboard/home.html')


def business_dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # If start_date and end_date are not provided, set them to the current year
    if not start_date or not end_date:
        current_year = date.today().year
        start_date = f'{current_year}-01-01'
        end_date = datetime.now().strftime(f'{current_year}-12-31')

    contracts = Contract.objects.filter(date__range=(start_date, end_date))
    revenue = sum(contract.income for contract in contracts)
    expenses = Expense.objects.filter(date__range=(start_date, end_date))
    total_expense = sum(expense.amount for expense in expenses)
    payroll_expenses = PayrollExpense.objects.filter(date__range=(start_date, end_date))
    total_payroll_expense = sum(payroll_expense.calculate_total_expense() for payroll_expense in payroll_expenses)
    travel_distance = sum(contract.travel_distance for contract in contracts)
    travel_expenses = Expense.objects.filter(date__range=(start_date, end_date), is_travel_allowance=True)
    total_travel_distance_paid = sum(expense.travel_distance for expense in travel_expenses)
    total_travel_allowance_expense = sum(expense.amount for expense in travel_expenses)
    net_income = revenue - (total_expense + total_payroll_expense)

    return render(request, 'dashboard/business_dashboard.html', {
        'start_date': start_date,
        'end_date': end_date,
        'revenue': revenue,
        'total_expense': total_expense,
        'total_payroll_expense': total_payroll_expense,
        'travel_distance': travel_distance,
        'total_travel_distance_paid': total_travel_distance_paid,
        'total_travel_allowance_expense': total_travel_allowance_expense,
        'net_income': net_income,
    })


def employee_dashboard(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # If start_date and end_date are not provided, set them to the current year
    if not start_date or not end_date:
        current_year = date.today().year
        start_date = f'{current_year}-01-01'
        end_date = datetime.now().strftime(f'{current_year}-12-31')

    payroll_expenses = PayrollExpense.objects.filter(
        employee=employee,
        date__range=(start_date, end_date)
    )

    federal_tax = sum(expense.federal_tax for expense in payroll_expenses)
    provincial_tax = sum(expense.provincial_tax for expense in payroll_expenses)
    cpp = sum(expense.cpp for expense in payroll_expenses)
    ei = sum(expense.ei for expense in payroll_expenses)
    income = sum(payroll_expense.calculate_total_expense() for payroll_expense in payroll_expenses) - (cpp + ei)
    net_income = income - (federal_tax + provincial_tax + cpp + ei)

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
