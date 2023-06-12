from rest_framework import serializers
from .models import StudentInfo, ExamInfo
from rest_framework.validators import UniqueValidator
from django.db.models import DateField


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ('first_name', 'last_name', 'roll_number', 'date_of_birth', 'department', 'year', 'created_at')
        extra_kwargs = {
            'roll_number': {'validators': []}  # Add any validators you want to apply to the roll_number field
        }
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamInfo
        fields = ('name', 'exam_date')

class ExamSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = ExamInfo
        fields = '__all__'
