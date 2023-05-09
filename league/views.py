from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import League, Group, GroupTeam
from .serializers import LeagueSerializer, GroupSerializer, GroupTeamSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupTeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = GroupTeam.objects.all()
    serializer_class = GroupTeamSerializer