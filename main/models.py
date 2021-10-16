#models.py File

from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=300)
    content= models.TextField()
    sex= models.CharField(max_length=20)
    vehicle1= models.CharField(max_length=200)
    vehicle2= models.CharField(max_length=200)
    vehicle3= models.CharField(max_length=200)
    # vehicle4= models.CharField(max_length=200)
    