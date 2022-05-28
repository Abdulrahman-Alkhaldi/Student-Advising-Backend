from rest_framework import serializers
from .admin import *

from .models import *


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('idd', 'year')

class ApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apointment
        fields = ('idd','date', 'time','location','reason','comment')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('idds','name','student_id','year', 'email','phonenumber')

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
    class meta:
        model = Registration
        fields = ('student','course','semister')