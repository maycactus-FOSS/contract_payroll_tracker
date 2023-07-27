# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_expense_list, name='payroll_expense_list'),
    path('create/', views.payroll_expense_create, name='payroll_expense_create'),
    path('update/<int:payroll_id>/', views.payroll_expense_update, name='payroll_expense_update'),
    path('delete/<int:payroll_id>/', views.payroll_expense_delete, name='payroll_expense_delete'),
]