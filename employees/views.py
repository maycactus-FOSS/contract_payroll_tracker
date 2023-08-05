# employees/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    clicked_column = request.GET.get('sort_column')

    sort_column = request.session.get('sort_column', 'pk')
    sort_order = request.session.get('sort_order', 'asc')

    if clicked_column:
        if sort_column != clicked_column:
            sort_column = clicked_column
            sort_order = 'asc'
        else:
            sort_order = 'asc' if sort_order == 'desc' else 'desc'

    request.session['sort_column'] = sort_column
    request.session['sort_order'] = sort_order

    if sort_order == 'asc':
        employees = Employee.objects.order_by(sort_column)
    else:
        employees = Employee.objects.order_by('-' + sort_column)

    items_per_page = int(request.GET.get('items_per_page', 10))
    
    paginator = Paginator(employees, items_per_page)
    page = request.GET.get('page')

    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    except EmptyPage:
        employees_page = paginator.page(paginator.num_pages)
    
    context = {
        'employees': employees_page,
        'items_per_page': items_per_page,
    }
    return render(request, 'employees/employee_list.html', context=context)

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_create_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_update_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    vacation_rate = employee.vacation_rate * 100

    return render(request, 'employees/employee_detail.html', {
        'employee': employee,
        'vacation_rate': vacation_rate
        })