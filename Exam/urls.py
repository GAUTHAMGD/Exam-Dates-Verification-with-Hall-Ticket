from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, HallTicketViewSet, HallticketListCreateView


router = DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('halltickets', HallTicketViewSet)

app_name = 'Exam'

urlpatterns = [
    path('', include(router.urls)),
    path('halltickets/', HallticketListCreateView.as_view(), name='hallticket-list-create'),
]






