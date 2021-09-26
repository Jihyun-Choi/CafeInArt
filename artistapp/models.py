from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='artist', null=True)

    name = models.CharField(max_length=200, null=True)
    category = models.TextField(null=True)  #분야
    phone_number = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)   #자기소개
    created_at = models.DateField(auto_now_add=True, null=True)

    image1 = models.ImageField(upload_to='artist/', null=False)
    image2 = models.ImageField(upload_to='artist/', null=True)
    image3 = models.ImageField(upload_to='artist/', null=True)
    image4 = models.ImageField(upload_to='artist/', null=True)


