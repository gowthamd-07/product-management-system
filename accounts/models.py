from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class User(AbstractUser):
    uploader = models.BooleanField(default=False)
    viewer = models.BooleanField(default=False)
    verifier = models.BooleanField(default=False)

    objects = UserManager()
    