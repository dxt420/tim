from django.db import models
import uuid


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


from django.utils import timezone
import datetime

 

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False,blank=True)
    is_super_admin = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.username
  

class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,blank=True)
    contact = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Admin(models.Model):
    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    contact = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    employee_shift_time = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.ForeignKey('Employee', on_delete=models.CASCADE)

class Vehicle(models.Model):
    vehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    license_plate = models.CharField(max_length=50,blank=True)
    vehicle_contact = models.CharField(max_length=50,blank=True)
    vehicle_color = models.CharField(max_length=50,blank=True)
    driver_name = models.CharField(max_length=50,blank=True)
    vehicle_description = models.CharField(max_length=500,blank=True)


    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.license_plate

class VehicleAvailability(models.Model):
    vehicle_plate = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.CASCADE)
    status = models.CharField(max_length=50,blank=True)

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.ForeignKey('Employee', on_delete=models.CASCADE)
    vehicle_plate = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    
    start_time = models.CharField(max_length=50,blank=True)
    end_time = models.CharField(max_length=50,blank=True)
    pickup_address = models.CharField(max_length=50,blank=True)
    dropoff_address = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name



class Report(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report_title = models.CharField(max_length=50,blank=True)
    report_details = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_title









