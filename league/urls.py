from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'leagues', views.LeagueViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'group-teams', views.GroupTeamViewSet)
router.register(r'match-days', views.MatchDayViewSet)

urlpatterns = router.urls
