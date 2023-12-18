from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.utils import timezone
from smsapi.managers import CustomUserManager

rolesChoices = [
    ('Admin', 'SuperAdmin'),
    ('SubAdmin', 'IntermediateAdmin'),
    ('BaseAdmin', 'BasicAdmin'),
    ('Student', 'Student'),
    ('Teacher', 'Teacher')
]

termChoices = [
    ('1', 'Term1'),
    ('2', 'Term2'),
    ('3', 'Term3')
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
    
    @property
    def tokens(self):
        pass


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
    
    @property
    def tokens(self):
        pass

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Term(models.Model):
    name = models.CharField(max_length=1, choices=termChoices, default=1)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
class Test(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=False, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class studentScore(models.Model):
    student = models.ForeignKey(Student, related_name="studentscore", on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.score
    
    class Meta:
        unique_together = ['student', 'test']

class studentPerformance(models.Model):
    gradeChoices = [
        ('NA', 'Not Graded'),
        ('A', 'Excellent'),
        ('B', 'Very Good'),
        ('C', 'Good'),
        ('D', 'Fair'),
        ('E', 'Fail'),
        ('F', 'Very Poor')
    ]

    student = models.ForeignKey(Student, related_name="studentperformance", on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=gradeChoices, default='NA')

    def __str__(self):
        return self.grade
    
    class Meta:
        unique_together = ['student', 'grade']