from django.core import validators
from django.db.models import fields
from django import forms
from django.forms.widgets import HiddenInput
from .models import StudentInfo,StudentAcademics


class StudentAcademicsForm(forms.ModelForm):
    
    class Meta:
        model=StudentAcademics
        fields = ['roll_no',
                  'maths',
                  'physics',
                  'chemistry',
                  'biology',
                  'english']
        exclude = ('roll_no',)
        widgets={'roll_no':forms.TextInput(attrs={'hidden':True,'required':False}),
                 'maths':forms.NumberInput(attrs={'class':'form-control'}),
                 'physics':forms.NumberInput(attrs={'class':'form-control'}),
                 'chemistry':forms.NumberInput(attrs={'class':'form-control'}),
                 'biology':forms.NumberInput(attrs={'class':'form-control'}),
                 'english':forms.NumberInput(attrs={'class':'form-control'})
                 }
    