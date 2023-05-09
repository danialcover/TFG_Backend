from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'leagues', views.LeagueViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'group-teams', views.GroupTeamViewSet)

urlpatterns = router.urls
