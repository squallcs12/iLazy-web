from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    coins = models.IntegerField(default=0)


class UserDevice(models.Model):
    IOS = 1

    user = models.ForeignKey(User)
    device_token = models.CharField(max_length=255)
    device_type = models.IntegerField(default=IOS)
