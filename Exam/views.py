from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Exam, HallTicket
from .serializers import StudentSerializer, ExamSerializer, HallTicketSerializer

class StudentCreateView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ExamCheckView(APIView):
    def post(self, request):
        roll_number = request.data.get('roll_number')
        date = request.data.get('date')

        try:
            student = Student.objects.get(roll_number=roll_number)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=404)

        try:
            exam = Exam.objects.get(date=date)
        except Exam.DoesNotExist:
            return Response({'message': 'No exams on this date.'}, status=200)

        if HallTicket.objects.filter(student=student, exam=exam).exists():
            return Response({'message': 'Student has an exam on this date.'}, status=200)
        else:
            return Response({'message': 'Student has no exam on this date.'}, status=200)

class HallTicketView(APIView):
    def get(self, request, roll_number):
        try:
            student = Student.objects.get(roll_number=roll_number)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=404)

        hall_tickets = HallTicket.objects.filter(student=student)
        serializer = HallTicketSerializer(hall_tickets, many=True)
        return Response(serializer.data, status=200)

class UpcomingExamView(APIView):
    def get(self, request, roll_number):
        try:
            student = Student.objects.get(roll_number=roll_number)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=404)

        upcoming_exams = Exam.objects.filter(date__gte=date.today()).order_by('date')[:5]
        serializer = ExamSerializer(upcoming_exams, many=True)
        return Response(serializer.data, status=200)
