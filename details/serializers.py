from rest_framework import serializers
from .models import StudentInfo, ExamInfo, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ('id', 'first_name', 'last_name', 'roll_number', 'date_of_birth', 'department', 'year', 'created_at')


class ExamInfoSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = ExamInfo
        fields = ('id', 'first_name', 'last_name', 'roll_number', 'date_of_birth', 'department', 'year', 'created_at', 'subjects')

    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects')
        exam_info = ExamInfo.objects.create(**validated_data)
        for subject_data in subjects_data:
            subject = Subject.objects.create(**subject_data)
            exam_info.subjects.add(subject)
        return exam_info
