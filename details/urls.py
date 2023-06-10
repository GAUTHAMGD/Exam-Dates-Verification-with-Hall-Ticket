from django.urls import path
from .views import studentViewSet
from . import views


urlpatterns = [
    path("studentViewSet/create", studentViewSet.as_view({"post": "create"})),
     path('my-url/', views.my_view, name='my_view'),
]


    
