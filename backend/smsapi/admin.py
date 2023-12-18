from django.contrib import admin
from smsapi.models import User, Teacher, Student, Test, Term, Subject, studentPerformance, studentScore

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Term)
admin.site.register(Subject)
admin.site.register(studentPerformance)
admin.site.register(studentScore)