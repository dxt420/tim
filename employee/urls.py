from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'employee'

urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.index, name="index"),
    path('managers', views.managers, name="managers"),
    path('new_manager', views.new_manager, name="new_manager"),
    path('manager_detail', views.manager_detail, name="manager_detail"),
    path('employees', views.employees, name="employees"),
    path('new_employee', views.new_employee, name="new_employee"),
    path('employee_detail', views.employee_detail, name="employee_detail"),
]