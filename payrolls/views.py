from django.shortcuts import render, get_object_or_404, redirect
from .models import PayrollExpense
from .forms import PayrollExpenseForm

def payroll_expense_list(request):
    expenses = PayrollExpense.objects.all()
    return render(request, 'payrolls/payroll_expense_list.html', {'expenses': expenses})

def payroll_expense_create(request):
    if request.method == 'POST':
        form = PayrollExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_expense_list')
    else:
        form = PayrollExpenseForm()
    return render(request, 'payrolls/payroll_expense_create_form.html', {'form': form})

def payroll_expense_update(request, payroll_id):
    expense = get_object_or_404(PayrollExpense, payroll_id=payroll_id)
    if request.method == 'POST':
        form = PayrollExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('payroll_expense_list')
    else:
        form = PayrollExpenseForm(instance=expense)
    return render(request, 'payrolls/payroll_expense_update_form.html', {'form': form})

def payroll_expense_delete(request, payroll_id):
    expense = get_object_or_404(PayrollExpense, payroll_id=payroll_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('payroll_expense_list')
    return render(request, 'payrolls/payroll_expense_confirm_delete.html', {'expense': expense})
