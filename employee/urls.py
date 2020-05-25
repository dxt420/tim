from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'employee'

urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.index, name="index"),





    

]