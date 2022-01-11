from django.contrib import admin
from django.db.models.fields import CommaSeparatedIntegerField
from .models import StudentInfo,StudentAcademics

# Register your models here.
@admin.register(StudentInfo)
class StudentAdmin(admin.ModelAdmin):
    data_list=('roll_no','name','school','class_name','mobile','addess')