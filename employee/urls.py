from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'employee'

urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.index, name="index"),
    path('vehicles', views.vehicles, name="vehicles"),
    path('new_vehicle', views.new_vehicle, name="new_vehicle"),
    path('add_vehicle', views.add_vehicle, name="add_vehicle"),
    path('vehicle_details/<slug:vehicle_id>', views.vehicle_details, name="vehicle_details"),
    path('edit_vehicle/<slug:vehicle_id>', views.edit_vehicle, name="edit_vehicle"),

    path('bookings', views.bookings, name="bookings"), 
    path('employees', views.employees, name="employees"),
    path('new_employee', views.new_employee, name="new_employee"),
    path('employee_detail', views.employee_detail, name="employee_detail"),
]