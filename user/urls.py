from django.urls import path
from . import views
from .views import profile_create

urlpatterns = [
    path('profiles/role/<int:role_id>/', views.ProfileListByRole.as_view(), name='profile-list-by-role'),
    path('profiles/create/', profile_create, name='profile-create')
]
