from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class GalleryCafe(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='gallerycafe', null=True)

    name = models.CharField(max_length=200, null=True)#카페이름
    image1 = models.ImageField(upload_to='main/', null=False) #홍보사진
    image2 = models.ImageField(upload_to='main/', null=False)
    image3 = models.ImageField(upload_to='main/', null=False)
    content = models.TextField(null=True) #카페소개

    created_at = models.DateField(auto_now_add=True, null=True)
