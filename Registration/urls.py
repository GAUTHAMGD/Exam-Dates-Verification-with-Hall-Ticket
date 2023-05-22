# django imports
from django.urls import path

# local imports
from .views import AuthUserViewSet

urlpatterns = [
    path("register/", AuthUserViewSet.as_view({"post": "register"})),
    path("login/", AuthUserViewSet.as_view({"post": "login"})),
    path("logout/", AuthUserViewSet.as_view({"post": "logout"})),
    
]
