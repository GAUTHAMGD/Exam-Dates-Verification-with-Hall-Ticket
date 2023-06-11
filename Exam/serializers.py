from rest_framework import serializers
from .models import Subject, Department, HallTicket, StudentInfo

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=50, unique=True)
    department = serializers.CharField(max_length=100, required= True)
    exam_date = serializers.DateField()
    year = serializers.PositiveIntegerField()



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    name = serializers.CharField(max_length=100)


class HallTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallTicket
        fields = '__all__'
    student = serializers.ForeignKey(StudentInfo, on_delete=serializers.CASCADE)
    subject = serializers.ForeignKey(Subject, on_delete=serializers.CASCADE)
    hall_ticket_number = serializers.CharField(max_length=20)
