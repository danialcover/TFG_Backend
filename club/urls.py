from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'members', views.MemberViewSet)

urlpatterns = router.urls
