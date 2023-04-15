from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'matches', views.MatchViewSet, basename='match')

urlpatterns = [
    path('matches/group/<int:group_id>/', views.MatchesByGroupView.as_view(), name='matches-by-group'),
] + router.urls
