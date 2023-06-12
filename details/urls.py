from django.urls import path
from .views import studentViewSet,subjectViewSet,examViewSet
from . import views
from .views import enter_registration_number


urlpatterns = [
   #3 path("studentViewSet/create", studentViewSet.as_view({"post": "create"})),
   # path("subjectViewSet/create",   subjectViewSet.as_view({"post": "create"})),
  #  path("examViewSet/create",  examViewSet.as_view({"post": "create"})),
  #  path('my-url/', views.my_view, name='my_view'),
    path('enter-registration/', enter_registration_number, name='enter_registration'),
]


    
