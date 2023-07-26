# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contracts/', include('contracts.urls')),
    path('employees/', include('employees.urls')),
    path('expenses/', include('expenses.urls')),
    path('dashboard/', include('dashboard.urls')),
]
