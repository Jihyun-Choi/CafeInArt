from django.contrib.auth.models import User
from django.db import models


class GalleryCafe(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='gallerycafe', null=True)

    name = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    location = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    image1 = models.ImageField(upload_to='main/', null=False)
    #image2 = models.ImageField(upload_to='main/', null=True)
    #image3 = models.ImageField(upload_to='main/', null=True)
    #image4 = models.ImageField(upload_to='main/', null=True)


