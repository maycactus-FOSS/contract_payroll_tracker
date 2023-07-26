# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_dashboard, name='default_dashboard'),
    path('business/', views.business_dashboard, name='business_dashboard'),
    path('employee/<int:employee_id>/', views.employee_dashboard, name='employee_dashboard'),
]
