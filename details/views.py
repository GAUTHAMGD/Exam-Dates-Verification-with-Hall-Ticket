from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Exam, Student, HallTicket
from .serializers import ExamSerializer, StudentSerializer, HallTicketSerializer
from django.shortcuts import render


class ExamListCreateView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class HallTicketListCreateView(generics.ListCreateAPIView):
    queryset = HallTicket.objects.all()
    serializer_class = HallTicketSerializer




from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from django.db import IntegrityError

def create_hallticket(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        exam_id = request.POST.get('exam_id')
        hall_ticket_number = request.POST.get('hall_ticket_number')

        try:
            student = get_object_or_404(Student, id=student_id)
            exam = get_object_or_404(Exam, id=exam_id)

            hall_ticket = HallTicket.objects.create(
                student=student,
                exam=exam,
                hall_ticket_number=hall_ticket_number
            )

            # Perform any other actions or redirect to a success page

        except IntegrityError:
            return HttpResponseServerError("Error: Failed to create hall ticket. Please check your input.")

    # Render the form for creating a hall ticket
    students = Student.objects.all()
    exams = Exam.objects.all()

    context = {
        'students': students,
        'exams': exams,
    }

    return render(request, 'create_hallticket.html', context)
