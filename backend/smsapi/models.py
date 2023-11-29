from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from smsapi.managers import CustomUserManager

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
    groups = models.ManyToManyField(Group, related_name='admins')
    user_permissions = models.ManyToManyField(Permission, related_name='admin_users')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Teacher(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=255, choices=rolesChoices, default='Teacher')
    teacherfullname = models.CharField(max_length=255, null=True)
    teachermobile = models.PositiveIntegerField(null=True, editable=True)
    entrysalary = models.PositiveIntegerField(null=True, default=0)
    salarypaid = models.PositiveIntegerField(null=True, editable=True)
    groups = models.ManyToManyField(Group, related_name='teachers')
    user_permissions = models.ManyToManyField(Permission, related_name='teacher_users')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    @property
    def salarybalance(self):
        balance = self.entrysalary - self.salarypaid
        return float(balance)


class Student(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=255, choices=rolesChoices, default='Student')
    studentfullname = models.CharField(max_length=255, null=True)
    studentmobile = models.PositiveIntegerField(null=True, editable=True)
    entryfee = models.PositiveIntegerField(null=True, default=0)
    feepaid = models.PositiveIntegerField(null=True, editable=True)
    groups = models.ManyToManyField(Group, related_name='students')
    user_permissions = models.ManyToManyField(Permission, related_name='student_users')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
    @property
    def feebalance(self):
        balance = float(self.entryfee) - float(self.feepaid)
        return float(balance)
    