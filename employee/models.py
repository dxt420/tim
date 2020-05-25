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
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    contact = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

