from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Match
from .serializers import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchesByGroupView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MatchSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Match.objects.filter(group_id=group_id)
