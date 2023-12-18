from rest_framework import serializers
from smsapi.models import User, Teacher, Student, Subject, studentPerformance, studentScore, Term, Test

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Teacher
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']

class StudentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Student
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Subject
        fields = '__all__'

class TermSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Term
        fields = '__all__'

    def create(self, validated_data):
        term = super().create(validated_data)
        self.generate_tests_for_term(term)
        return term
    
    def generate_tests_for_term(self, term):
        # Assuming a list of subjects is in place
        subjects = Subject.objects.all()

        for subject in subjects:
            for test_number in range(1, 3):
                test_name = f"{subject.name} {chr(ord('A') + test_number - 1)}"
                Test.objects.create(term=term, subject=subject, name=test_name)