from rest_framework import generics
from .models import StudentInfo
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ViewSet
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class studentViewSet(ViewSet):
    def create(self, request):
        data = request.data
        data.update({"user": request.user.id})
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
def my_view(request):
    if request.method == 'POST':
        # Handle the POST request
        return HttpResponse('This is a POST request.')
    elif request.method == 'GET':
        # Handle the GET request
        return HttpResponse('This is a GET request.')
    else:
        # Handle other HTTP methods
        return HttpResponse('This is a different HTTP method.')

       
class StudentCreateView(APIView):
    # view logic for creating a student
    pass

class ExamCheckView(APIView):
    # view logic for checking exam
    pass

class HallTicketView(APIView):
    # view logic for hall ticket
    pass

class UpcomingExamView(APIView):
    # view logic for upcoming exams
    pass