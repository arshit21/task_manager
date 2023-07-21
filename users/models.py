from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

