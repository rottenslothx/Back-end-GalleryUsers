from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    gender = models.CharField(default='male', max_length=5)

