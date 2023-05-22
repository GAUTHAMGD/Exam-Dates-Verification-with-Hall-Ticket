from rest_framework import generics
from .models import StudentInfo
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class studentViewSet(ViewSet):
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

#class subjectViewSet(ViewSet):
    def create(self, request):
        serializer = subjectSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


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