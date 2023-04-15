from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'matches', views.MatchViewSet)

urlpatterns = [
    path('matches/<int:group_id>/', views.MatchesByGroupView.as_view(), name='matches_by_group'),
]

urlpatterns += router.urls
