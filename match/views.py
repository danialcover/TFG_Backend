from rest_framework import viewsets

from league.views import CustomGetPermissions
from .models import Match
from .serializers import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomGetPermissions,)
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
