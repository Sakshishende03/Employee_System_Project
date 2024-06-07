"""
URL configuration for office_employee_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from emp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('all_emp/', views.all_emp),
    path('add_emp/', views.add_emp),
    path('remove_emp/', views.remove_emp),
    path('remove_emp/<int:emp_id>', views.remove_emp),
    path('filter_emp/', views.filter_emp, name='filter_emp'),  # Ensure the URL ends with a slash


]
