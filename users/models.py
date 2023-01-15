from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=120,blank=False)
    email = models.EmailField(max_length=120,blank=False,unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name


def upload_pic(instance, filename):
    return 'image/{filename}'.format(filename=filename)

class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='profile_name')
    profile_pic =models.ImageField(upload_to=upload_pic,default='image/default.jpg')
    username= models.CharField(max_length=150)
    bio = models.CharField(max_length=250)
    created_at =models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)