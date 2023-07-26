# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.operating_expense_list, name='operating_expense_list'),
    path('create/', views.operating_expense_create, name='operating_expense_create'),
    path('update/<int:expense_id>/', views.operating_expense_update, name='operating_expense_update'),
    path('delete/<int:expense_id>/', views.operating_expense_delete, name='operating_expense_delete'),
]
