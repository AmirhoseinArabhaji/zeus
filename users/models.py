from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin
