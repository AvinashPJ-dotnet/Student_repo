from rest_framework import serializers
from . import models

class StudentInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentInfo
        fields=(
            'roll_no',
            'name',
            'class_name',
            'school',
            'mobile',
            'address'
        )

class StudentAcademicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAcademics
        fields=(
            'id',
            'roll_no',
            'maths',
            'physics',
            'chemistry',
            'biology',
            'english'
            
        )