from django.db import models
from rest_framework.fields import DateField
import email
import django
import datetime

now = datetime.datetime.now()
YEAR_CHOICES = []
for r in range(2008, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Curriculum(models.Model):
    idd = models.IntegerField(blank=False)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    def __str__(self):
        return f"{self.year}"

class Advisor(models.Model):
    idd = models.IntegerField(blank=False)
    name = models.CharField(max_length=120)
    def __str__(self):
        return f"{self.name}"

class Semester(models.Model):
    term = models.CharField(max_length=120)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    startdate = models.DateField(max_length=120)
    enddate = models.DateField(max_length=120)
    def __str__(self):
        return f"{self.term} {self.year}"
    pass

class Student(models.Model):
    name = models.CharField(max_length=120)
    student_id = models.IntegerField(blank=False,null=True)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=1)
    email = models.EmailField(blank=False,null= True)
    phonenumber = models.IntegerField(blank=False)
    idds = models.ForeignKey(Curriculum,on_delete=models.PROTECT,blank=False,null=True)
    def __str__(self):
        return f"{self.name} {self.student_id}"

class Apointment(models.Model):
    idd = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    date = models.DateField(max_length=120)
    time = models.TimeField(blank=False)
    location = models.CharField(max_length=300)
    reason = models.CharField(max_length=120)
    comment = models.CharField(max_length=120, blank=True)
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE,blank=False,null=True)
    def __str__(self):
        return f"{self.time} {self.date} {self.idd}"
    pass

class Courses(models.Model):
    idds = models.ManyToManyField(Curriculum, blank=True)
    name = models.CharField(max_length=120, blank=False,null=True) 
    number = models.IntegerField(blank=False,null=True)
    credits = models.IntegerField(blank=False,null=True) 
    pre_requisites = models.CharField(max_length=120, blank=True,null=True) 
    co_requisites = models.CharField(max_length=120, blank=True,null=True) 
    description= models.CharField(max_length=120)
    def __str__(self):
        return f"{self.number} {self.name}"

class Registration(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT,blank=False,null=True)
    course = models.ForeignKey(Courses,on_delete=models.PROTECT,blank=False,null=True)
    semister = models.ForeignKey(Semester,on_delete=models.PROTECT,blank=False,null=True)
    def __str__(self):
        return f"{self.student} {self.semister}"