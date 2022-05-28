from django.shortcuts import render
from rest_framework import viewsets
import json

from .models import *
from .serializers import *
# Create your views here.

class CurriculumView(viewsets.ModelViewSet):
    serializer_class = CurriculumSerializer
    queryset = Curriculum.objects.all()

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class AdvisorView(viewsets.ModelViewSet):
    serializer_class = AdvisorSerializer
    queryset = Advisor.objects.all()

class ApointmentView(viewsets.ModelViewSet):
    serializer_class = ApointmentSerializer
    queryset = Apointment.objects.all()

class SemesterView(viewsets.ModelViewSet):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()

class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

class RegistrationView(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()