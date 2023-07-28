from django.shortcuts import render, get_object_or_404, redirect
from .models import PayrollExpense
from .forms import PayrollExpenseForm

def payroll_expense_list(request):
    payroll_expenses = PayrollExpense.objects.all()
    return render(request, 'payrolls/payroll_expense_list.html', {'payroll_expenses': payroll_expenses})

def payroll_expense_create(request):
    if request.method == 'POST':
        form = PayrollExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_expense_list')
    else:
        form = PayrollExpenseForm()
    return render(request, 'payrolls/payroll_expense_create_form.html', {'form': form})

def payroll_expense_update(request, pk):
    payroll_expense = get_object_or_404(PayrollExpense, pk=pk)
    if request.method == 'POST':
        form = PayrollExpenseForm(request.POST, instance=payroll_expense)
        if form.is_valid():
            form.save()
            return redirect('payroll_expense_list')
    else:
        form = PayrollExpenseForm(instance=payroll_expense)
    return render(request, 'payrolls/payroll_expense_update_form.html', {'form': form})

def payroll_expense_delete(request, pk):
    payroll_expense = get_object_or_404(PayrollExpense, pk=pk)
    if request.method == 'POST':
        payroll_expense.delete()
        return redirect('payroll_expense_list')
    return render(request, 'payrolls/payroll_expense_confirm_delete.html', {'payroll_expense': payroll_expense})
