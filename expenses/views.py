from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    clicked_column = request.GET.get('sort_column')

    sort_column = request.session.get('sort_column', 'date')
    sort_order = request.session.get('sort_order', 'desc')

    if clicked_column:
        if sort_column != clicked_column:
            sort_column = clicked_column
            sort_order = 'asc' if sort_column == 'description' else 'desc'
        else:
            sort_order = 'asc' if sort_order == 'desc' else 'desc'

    request.session['sort_column'] = sort_column
    request.session['sort_order'] = sort_order

    if sort_order == 'asc':
        expenses = Expense.objects.order_by(sort_column)
    else:
        expenses = Expense.objects.order_by('-' + sort_column)
    items_per_page = int(request.GET.get('items_per_page', 10))
    
    paginator = Paginator(expenses, items_per_page)
    page = request.GET.get('page')

    try:
        expenses_page = paginator.page(page)
    except PageNotAnInteger:
        expenses_page = paginator.page(1)
    except EmptyPage:
        expenses_page = paginator.page(paginator.num_pages)
    
    context = {
        'expenses': expenses_page,
        'items_per_page': items_per_page,
    }
    return render(request, 'expenses/expense_list.html', context=context)

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_create_form.html', {'form': form})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_update_form.html', {'form': form})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'expenses/expense_detail.html', {'expense': expense})