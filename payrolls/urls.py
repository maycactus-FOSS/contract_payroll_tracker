# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_expense_list, name='payroll_expense_list'),
    path('<int:pk>/', views.payroll_expense_detail, name='payroll_expense_detail'),
    path('create/', views.payroll_expense_create, name='payroll_expense_create'),
    path('update/<int:pk>/', views.payroll_expense_update, name='payroll_expense_update'),
    path('delete/<int:pk>/', views.payroll_expense_delete, name='payroll_expense_delete'),
]
