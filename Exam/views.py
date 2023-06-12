from rest_framework import generics
from rest_framework import viewsets
from .models import Subject, HallTicket
from .serializers import SubjectSerializer, HallTicketSerializer



class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class HallTicketViewSet(viewsets.ModelViewSet):
    queryset = HallTicket.objects.all()
    serializer_class = HallTicketSerializer


class HallticketListCreateView(generics.ListCreateAPIView):
    queryset = HallTicket.objects.all()
    serializer_class = HallTicketSerializer


    