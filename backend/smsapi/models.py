from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

rolesChoices = [
    ('Admin', 'SuperAdmin'),
    ('SubAdmin', 'IntermediateAdmin'),
    ('BaseAdmin', 'BasicAdmin'),
    ('Student', 'Student'),
    ('Teacher', 'Teacher')
]

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=255, choices=rolesChoices, default='BaseAdmin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    teachername = models.CharField(max_length=255, null=True)
    teachermobile = models.PositiveIntegerField(null=True, editable=True)
    entrysalary = models.PositiveIntegerField(null=True, default=0)
    salarypaid = models.PositiveIntegerField(null=True, editable=True)


    def __str__(self) -> str:
        return self.user.id

    @property
    def salarybalance(self):
        balance = self.entrysalary - self.salarypaid
        return balance


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    studentname = models.CharField(max_length=255, null=True)
    studentmobile = models.PositiveIntegerField(null=True, editable=True)
    entryfee = models.PositiveIntegerField(null=True, default=0)
    feepaid = models.PositiveIntegerField(null=True, editable=True)

    def __str__(self) -> str:
        return self.user.id
    
    @property
    def feebalance(self):
        balance = self.entryfee - self.feepaid
        return balance
    