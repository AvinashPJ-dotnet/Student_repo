from django.core import validators
from django.db.models import fields
from django import forms
from django.forms.widgets import HiddenInput
from .models import StudentInfo,StudentAcademics

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
        
# class StudentAcademicsForm(forms.ModelForm):
    
#     class Meta:
#         model=StudentAcademics
#         fields = ['roll_no',
#                   'maths',
#                   'physics',
#                   'chemistry',
#                   'biology',
#                   'english']
#         exclude = ('roll_no',)
#         widgets={'roll_no':forms.TextInput(attrs={'hidden':True,'required':False}),
#                  'maths':forms.NumberInput(attrs={'class':'form-control'}),
#                  'physics':forms.NumberInput(attrs={'class':'form-control'}),
#                  'chemistry':forms.NumberInput(attrs={'class':'form-control'}),
#                  'biology':forms.NumberInput(attrs={'class':'form-control'}),
#                  'english':forms.NumberInput(attrs={'class':'form-control'})
#                  }
    