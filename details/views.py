from rest_framework import generics
from .models import StudentInfo,ExamInfo
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ViewSet
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from .models import StudentInfo

class studentViewSet(ViewSet):
    def create(self, request):
        data = request.data
        data.update({"user": request.user.id})
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

class subjectViewSet(ViewSet):
    def create(self, request):
        data = request.data
        data.update({"user": request.user.id})
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)    
    
class examViewSet(ViewSet):
    def create(self, request):
        data = request.data
        data.update({"user": request.user.id})
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            exam = serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)    

def enter_registration_number(request):
    if request.method == 'POST':
        registration_number = request.POST.get('registration_number')
        try:
            student = StudentInfo.objects.get(registration_number=registration_number)
            subjects = student.subjects.all()
            return render(request, 'subject_list.html', {'subjects': subjects})
        except StudentInfo.DoesNotExist:
            return render(request, 'invalid_registration.html')
    return render(request, 'enter_registration.html')

#def my_view(request):
#    if request.method == 'POST':
#        # Handle the POST request
#        return HttpResponse('This is a POST request.')
 #   elif request.method == 'GET':
#        # Handle the GET request
#        return HttpResponse('This is a GET request.')
#    else:
#       # Handle other HTTP methods
#        return HttpResponse('This is a different HTTP method.')

       
# class StudentCreateView(APIView):
#     # view logic for creating a student
#     pass

# class ExamCheckView(APIView):
#     # view logic for checking exam
#     pass

# class HallTicketView(APIView):
#     # view logic for hall ticket
#     pass

# class UpcomingExamView(APIView):
#     # view logic for upcoming exams
#     pass