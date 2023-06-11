from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentViewSet.as_view({'post': 'create'}), name='student-create'),
    path('myview/', views.MyView.as_view(), name='my-view'),
    path('student-create/', views.StudentCreateView.as_view(), name='student-create-view'),
    path('exam-check/', views.ExamCheckView.as_view(), name='exam-check-view'),
    path('hall-ticket/', views.HallTicketView.as_view(), name='hall-ticket-view'),
    path('upcoming-exam/', views.UpcomingExamView.as_view(), name='upcoming-exam-view'),
]
