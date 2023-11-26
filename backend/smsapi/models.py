from django.db import models
from django.contrib.auth.models import AbstractUser

rolesChoices = [
    ('Admin', 'SuperAdmin'),
    ('SubAdmin', 'IntermediateAdmin'),
    ('BaseAdmin', 'BasicAdmin')
]

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=255, choices=rolesChoices, default='BaseAdmin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']