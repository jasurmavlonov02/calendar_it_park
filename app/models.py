from django.contrib.auth.models import AbstractUser
from django.db import models

from app.managers import UserManager


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=False)
    email = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
