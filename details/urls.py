from django.urls import path
from .views import ExamListCreateView, StudentListCreateView, HallTicketListCreateView, create_hallticket


app_name = 'hallticket'
urlpatterns = [
    path('exams/', ExamListCreateView.as_view()),
    path('students/', StudentListCreateView.as_view()),
    path('halltickets/', HallTicketListCreateView.as_view()),
    path('create/', create_hallticket, name='create'),
]


