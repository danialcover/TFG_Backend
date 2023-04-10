from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import League, Group
from .serializers import LeagueSerializer, GroupSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
