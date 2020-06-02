from django.shortcuts import render

from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponseRedirect

from . models import *


from django.conf import settings
from django.dispatch import receiver
from django.http import HttpRequest
from django.middleware.csrf import get_token

from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from django.http import JsonResponse
# from django.shortcuts import render_to_response



@login_required
def index(request):
    context = {
        "a":"mm-active"
    }
    return render(request,"employee/admin/dashboard.html",context)


def managers(request):
    context = {
        "ba":"mm-active"
    }
    return render(request,"employee/admin/managers.html",context)


def new_manager(request):
    context = {
        "bb":"mm-active"
    }
    return render(request,"employee/admin/new-manager.html",context)


def manager_detail(request):
    context = {
        "b":"mm-active"
    }
    return render(request,"employee/admin/manager-detail.html",context)

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



