from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    Profile_user=models.OneToOneField(user,on_delete=models.CASCADE)
    address=models.TextField()
    Profile_pic=models.ImageField(upload_to='abcd')