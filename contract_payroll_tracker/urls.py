# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contracts/', include('contracts.urls')),
    path('employees/', include('employees.urls')),
    path('payrolls/', include('payrolls.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('dashboard.urls')),  # Add default view for dashboard
]
