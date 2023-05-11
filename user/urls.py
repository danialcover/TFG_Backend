from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import profile_create, profile_delete

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
                  path('profiles/referees/', views.ProfileRefereesList.as_view(), name='profile-list-by-role'),
                  path('profiles/create/', profile_create, name='profile-create'),
                  path('profiles/delete/<int:pk>', profile_delete, name='profile-delete'),
                  path('roles', views.RoleListView.as_view(), name='role-list'),
                  path('login', views.login, name='login'),
              ] + router.urls
