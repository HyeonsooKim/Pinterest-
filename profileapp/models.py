from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    #profile과 user 객체를 하나씩 연결해준다
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    #profile picture, media/profile/에 저장됨, 없어도 괜찮다.
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

