from django.urls import path, include

# Used to have in the same base url all the apis for the data
urlpatterns = [
    path('', include('user.urls')),
    path('', include('league.urls')),
    path('', include('club.urls')),
    path('', include('match.urls')),
]