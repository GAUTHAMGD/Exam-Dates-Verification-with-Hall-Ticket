from django.urls import path
from .views import StudentViewSet,SubjectViewSet,ExamViewSet
from . import views
from .views import enter_registration_number


urlpatterns = [
    path("studentViewSet/create", StudentViewSet.as_view({"post": "create"})),
    path("subjectViewSet/create",   SubjectViewSet.as_view({"post": "create"})),
    path("examViewSet/create",  ExamViewSet.as_view({"post": "create"})),
    path('enter-registration/', enter_registration_number, name='enter_registration'),
    path('my-url/', views.my_view, name='my_view'),
    
]


    
