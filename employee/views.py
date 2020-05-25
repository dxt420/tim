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



# @login_required
def index(request):
    return render(request,"employee/admin/dashboard.html")