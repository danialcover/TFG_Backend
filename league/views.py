import json

from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import League, Group, GroupTeam, MatchDay
from .serializers import LeagueSerializer, GroupSerializer, GroupTeamSerializer, MatchDaySerializer


class CustomGetPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated


class LeagueViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupTeamViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = GroupTeam.objects.all()
    serializer_class = GroupTeamSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        match_outcomes = request.data.get('match_outcomes')
        if match_outcomes is not None:
            match_outcomes = json.loads(match_outcomes)
            serializer.validated_data['match_outcomes'] = match_outcomes

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        group_team_id = kwargs['pk']
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        match_outcomes = request.data.get('match_outcomes')
        if match_outcomes is not None:
            match_outcomes = json.loads(match_outcomes)
            serializer.instance.match_outcomes = match_outcomes

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(serializer.data)


class MatchDayViewSet(viewsets.ModelViewSet):
    queryset = MatchDay.objects.all()
    serializer_class = MatchDaySerializer
