from rest_framework import serializers
from .models import Subject, Department, HallTicket

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class HallTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallTicket
        fields = '__all__'
