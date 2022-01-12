from django.db import models

from django.utils.text import slugify

# Create your models here.
class StudentInfo(models.Model):
    roll_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30, blank=True)
    class_name=models.CharField(max_length=10,blank=True)
    school=models.CharField(max_length=30,blank=True)
    mobile=models.CharField(max_length=12,blank=True)
    address=models.TextField(blank=True)
    
class StudentAcademics(models.Model):
    roll_no=models.ForeignKey(StudentInfo,on_delete=models.SET_NULL,null=True)
    maths=models.IntegerField(blank=True)
    physics=models.IntegerField(blank=True)
    chemistry=models.IntegerField(blank=True)
    biology=models.IntegerField(blank=True)
    english=models.IntegerField(blank=True)
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.roll_no)
    #     super(StudentAcademics, self).save(*args, **kwargs)