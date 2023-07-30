# contracts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('<int:pk>/', views.contract_detail, name='contract_detail'),
    path('create/', views.contract_create, name='contract_create'),
    path('update/<int:pk>/', views.contract_update, name='contract_update'),
    path('delete/<int:pk>/', views.contract_delete, name='contract_delete'),
]
