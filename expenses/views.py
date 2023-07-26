# expenses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import OperatingExpense
from .forms import OperatingExpenseForm

def operating_expense_list(request):
    expenses = OperatingExpense.objects.all()
    return render(request, 'expenses/operating_expense_list.html', {'expenses': expenses})

def operating_expense_create(request):
    if request.method == 'POST':
        form = OperatingExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operating_expense_list')
    else:
        form = OperatingExpenseForm()
    return render(request, 'expenses/operating_expense_create_form.html', {'form': form})

def operating_expense_update(request, expense_id):
    expense = get_object_or_404(OperatingExpense, id=expense_id)
    if request.method == 'POST':
        form = OperatingExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('operating_expense_list')
    else:
        form = OperatingExpenseForm(instance=expense)
    return render(request, 'expenses/operating_expense_update_form.html', {'form': form})

def operating_expense_delete(request, expense_id):
    expense = get_object_or_404(OperatingExpense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('operating_expense_list')
    return render(request, 'expenses/operating_expense_confirm_delete.html', {'expense': expense})
