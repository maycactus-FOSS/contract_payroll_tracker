# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('business/', views.business_dashboard, name='business_dashboard'),
    path('employee/<int:pk>/', views.employee_dashboard, name='employee_dashboard'),
]
