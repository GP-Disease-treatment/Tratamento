from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=255)
    CPF = models.CharField(max_length=14, unique=True)

    USERNAME_FIELD = 'CPF'
    REQUIRED_FIELDS = ['name',]
    last_name = None
    first_name = None
    objects = UserManager()