from django.urls import path
from details.views import StudentCreateView, ExamCheckView, HallTicketView, UpcomingExamView

urlpatterns = [
    path('api/student/', StudentCreateView.as_view()),
    path('api/exam/check/', ExamCheckView.as_view()),
    path('api/hallticket/<str:roll_number>/', HallTicketView.as_view()),
    path('api/upcoming/<str:roll_number>/', UpcomingExamView.as_view()),
    path('create-student/', StudentCreateView.as_view(), name='create-student'),
]




urlpatterns = [
    path('create-student/', StudentCreateView.as_view(), name='create-student'),
     path('exam-check/', ExamCheckView.as_view(), name='exam-check'),
      path('hall-ticket/', HallTicketView.as_view(), name='hall-ticket'),
       path('upcoming-exams/', UpcomingExamView.as_view(), name='upcoming-exams'),
]
    # other URL patterns







