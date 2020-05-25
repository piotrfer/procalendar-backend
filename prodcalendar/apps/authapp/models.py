from django.db import models
from django.contrib.auth.models import AbstractUser
from ..week.models import Week

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    week = models.OneToOneField(Week, on_delete= models.CASCADE, null=True, blank=True)
    REQUIRED_FIELDS = ['username', 'first_name']
    USERNAME_FIELD = 'email'
