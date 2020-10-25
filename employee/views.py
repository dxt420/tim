from django.shortcuts import render

from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponseRedirect

from . models import *


from django.conf import settings
from django.dispatch import receiver
from django.http import HttpRequest
from django.middleware.csrf import get_token

from django.contrib.auth.decorators import login_required

from django.contrib import messages, auth

from django.db import IntegrityError
from django.http import JsonResponse
# from django.shortcuts import render_to_response



@login_required
def index(request):
    context = {
        "a":"mm-active"
    }
    return render(request,"employee/admin/dashboard.html",context)

def bookings(request):
    vehicles = Vehicle.objects.all()
    context = {
        "fa":"mm-active",
        "vehicles": vehicles
    }

    return render(request,"employee/admin/bookings.html",context)

def vehicles(request):
    vehicles = Vehicle.objects.all()
    context = {
        "ba":"mm-active",
        "vehicles": vehicles
    }

    return render(request,"employee/admin/vehicles.html",context)


def new_vehicle(request):
    context = {
        "bb":"mm-active"
    }
    return render(request,"employee/admin/new-vehicle.html",context)


def add_vehicle(request):
    if request.method == 'POST':
      
        new_vehicle = Vehicle(
            license_plate=request.POST['license_plate'],
            vehicle_contact=request.POST['vehicle_contact'],
            vehicle_color=request.POST['vehicle_color'])

        new_vehicle.save()
                
        messages.success(request, "a")
        request.session['foo'] = 2
        return HttpResponseRedirect(reverse('employee:vehicles'))





 


def vehicle_details(request,vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    context = {
    
         "ba":"mm-active",
        'vehicle': vehicle
    }
    return render(request,"employee/admin/vehicle-details.html",context)


def edit_vehicle(request,vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    vehicle.license_plate=request.POST['license_plate']
    vehicle.vehicle_contact=request.POST['vehicle_contact']
    vehicle.vehicle_color=request.POST['vehicle_color']
    vehicle.driver_name=request.POST['driver_name']
    vehicle.vehicle_description=request.POST['vehicle_description']
    
    vehicle.save()
    return HttpResponseRedirect(reverse('employee:vehicle_details', kwargs={'vehicle_id':vehicle_id}))
    # return render(request,"employee/admin/vehicle-details.html",context)

def employees(request):
    context = {
        "ca":"mm-active"
    }
    return render(request,"employee/admin/employees.html",context)


def new_employee(request):
    context = {
        "cb":"mm-active"
    }
    return render(request,"employee/admin/new-employee.html",context)


def employee_detail(request):
    context = {
        "c":"mm-active"
    }
    return render(request,"employee/admin/employee-detail.html",context)



