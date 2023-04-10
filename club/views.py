from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Club, Team, Location
from .serializers import ClubSerializer, TeamSerializer, LocationSerializer


class ClubViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
