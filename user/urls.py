from django.urls import path
from . import views
from .views import profile_create, profile_delete

urlpatterns = [
    path('profiles/<int:role_id>/', views.ProfileListByRole.as_view(), name='profile-list-by-role'),
    path('profiles/create/', profile_create, name='profile-create'),
    path('profiles/<int:pk>/delete/', profile_delete, name='profile-delete')
]
