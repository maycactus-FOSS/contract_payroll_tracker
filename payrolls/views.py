from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PayrollExpense
from .forms import PayrollExpenseForm

def payroll_expense_list(request):
    clicked_column = request.GET.get('sort_column')

    sort_column = request.session.get('sort_column', 'date')
    sort_order = request.session.get('sort_order', 'desc')

    if clicked_column:
        if sort_column != clicked_column:
            sort_column = clicked_column
            sort_order = 'asc' if sort_column == 'employee.name' else 'desc'
        else:
            sort_order = 'asc' if sort_order == 'desc' else 'desc'

    request.session['sort_column'] = sort_column
    request.session['sort_order'] = sort_order

    if sort_order == 'asc':
        payroll_expenses = PayrollExpense.objects.order_by(sort_column)
    else:
        payroll_expenses = PayrollExpense.objects.order_by('-' + sort_column)

    items_per_page = int(request.GET.get('items_per_page', 10))
    
    paginator = Paginator(payroll_expenses, items_per_page)
    page = request.GET.get('page')

    try:
        payroll_expenses_page = paginator.page(page)
    except PageNotAnInteger:
        payroll_expenses_page = paginator.page(1)
    except EmptyPage:
        payroll_expenses_page = paginator.page(paginator.num_pages)

    context = {
        'payroll_expenses': payroll_expenses_page,
        'items_per_page': items_per_page,
    }
    return render(request, 'payrolls/payroll_expense_list.html', context=context)

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

def payroll_expense_detail(request, pk):
    payroll_expense = get_object_or_404(PayrollExpense, pk=pk)

    total_expense = payroll_expense.calculate_total_expense()
    total_remittance = payroll_expense.calculate_total_remittance()
    net_payment = total_expense - total_remittance

    return render(request, 'payrolls/payroll_expense_detail.html', {
        'payroll_expense': payroll_expense,
        'total_expense': total_expense,
        'total_remittance': total_remittance,
        'net_payment': net_payment,
    })