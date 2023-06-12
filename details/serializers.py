from rest_framework import serializers
from .models import Exam, Student, HallTicket

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'subject', 'date']

class StudentSerializer(serializers.ModelSerializer):
    exams = ExamSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_number', 'exams']

class HallTicketSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    exam = ExamSerializer(read_only=True)

    class Meta:
        model = HallTicket
        fields = ['id', 'student', 'exam', 'hall_ticket_number']
