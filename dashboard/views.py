# dashboard/views.py
from django.shortcuts import render, get_object_or_404
from contracts.models import Contract
from employees.models import Employee
from expenses.models import Expense
from payrolls.models import PayrollExpense


def home(request):
    return render(request, 'dashboard/home.html')


def business_dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    contracts = Contract.objects.filter(date__range=(start_date, end_date))
    revenue = sum(contract.income for contract in contracts)
    expenses = Expense.objects.filter(date__range=(start_date, end_date))
    total_expense = sum(expense.amount for expense in expenses)
    payroll_expenses = PayrollExpense.objects.filter(date__range=(start_date, end_date))
    total_payroll_expense = sum(payroll_expense.calculate_total_expense() for payroll_expense in payroll_expenses)
    travel_distance = sum(contract.travel_distance for contract in contracts)
    net_income = revenue - (total_expense + total_payroll_expense)

    return render(request, 'dashboard/business_dashboard.html', {
        'start_date': start_date,
        'end_date': end_date,
        'revenue': revenue,
        'total_expense': total_expense,
        'total_payroll_expense': total_payroll_expense,
        'travel_distance': travel_distance,
        'net_income': net_income,
    })


def employee_dashboard(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    payroll_expenses = PayrollExpense.objects.filter(
        employee=employee,
        date__range=(start_date, end_date)
    )

    income = sum(payroll_expense.calculate_total_expense() for payroll_expense in payroll_expenses)
    federal_tax = sum(expense.federal_tax for expense in payroll_expenses)
    provincial_tax = sum(expense.provincial_tax for expense in payroll_expenses)
    cpp = sum(expense.cpp for expense in payroll_expenses)
    ei = sum(expense.ei for expense in payroll_expenses)
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
