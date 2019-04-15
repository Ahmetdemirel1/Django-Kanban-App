from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class User_register(models.Model):
    username = models.OneToOneField(User, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=32)
