from rest_framework import viewsets

from league.views import CustomGetPermissions
from .models import Club, Team, Location, Member
from .serializers import ClubSerializer, TeamSerializer, LocationSerializer, MemberSerializer


class ClubViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
