from django.urls import path
from . import views
from .views import profile_create, profile_delete

urlpatterns = [
    path('profiles/referees/', views.ProfileRefereesList.as_view(), name='profile-list-by-role'),
    path('profiles/create/', profile_create, name='profile-create'),
    path('profiles/<int:pk>/delete/', profile_delete, name='profile-delete'),
    path('roles', views.RoleListView.as_view(), name='role-list')
]
