from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'matches', views.MatchViewSet, basename='match')

urlpatterns = router.urls
