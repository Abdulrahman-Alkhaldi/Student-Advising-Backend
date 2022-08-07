from rest_framework import serializers
from .admin import *

from .models import *

'''this script is used to create the serializers for the todo app'''
'''a serializer is a class that converts the model into a json object'''
class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('idd', 'year')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('idds','name','student_id','year', 'email','phonenumber')

class ApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apointment
        fields = ('idd','date', 'time','location','reason','comment','studentID')

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('idd', 'name')
    
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('name','number', 'credits','pre_requisites','co_requisites','description')

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('term','year','startdate','enddate')
    
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('student','course','semister','idd')