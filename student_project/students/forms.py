from django.core import validators
from django.db.models import fields
from django import forms
from .models import StudentInfo

# class StudentRegistartion(forms.Form):
class StudentRegistartion(forms.ModelForm):
    
    class Meta:
        model=StudentInfo
        fields = ['name',
            'class_name',
            'school',
            'mobile',
            'address']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'class_name':forms.TextInput(attrs={'class':'form-control'}),
                 'school':forms.TextInput(attrs={'class':'form-control'}),
                 'mobile':forms.TextInput(attrs={'class':'form-control'}),
                 'address':forms.Textarea(attrs={'class':'form-control'})
                 }
    