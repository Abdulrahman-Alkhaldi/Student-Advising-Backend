from django.contrib import admin

from . import models 
# explain what this script is doing
'''this script is used to create the admin page for the todo app'''
'''classes that handle the admin page'''
class Apointment(admin.ModelAdmin):
    list_display = ('idd','date', 'time','location','reason','comment','studentID')

class Student(admin.ModelAdmin):
    list_display = ('idds', 'name','student_id','year','email','phonenumber')

class Advisor(admin.ModelAdmin):
    list_display = ('idd', 'name')

class Curriculum(admin.ModelAdmin):
    list_display = ('idd', 'year')
    
class Courses(admin.ModelAdmin):
    list_display = ('name','number', 'credits','pre_requisites','co_requisites','description')

class Semester(admin.ModelAdmin):
   list_display = ('term','year','startdate','enddate')
    
class Registration(admin.ModelAdmin):
    list_display = ('student','course','semister','idd')
# Register your models here.

admin.site.register(models.Registration)
admin.site.register(models.Curriculum)
admin.site.register(models.Courses)
admin.site.register(models.Advisor)
admin.site.register(models.Student)
admin.site.register(models.Semester)
admin.site.register(models.Apointment)