from rest_framework import serializers

from club.serializers import TeamSerializer, LocationSerializer
from league.serializers import GroupSerializer
from user.serializers import ProfileSerializer
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    user = ProfileSerializer()
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    location = LocationSerializer()
    date = serializers.DateTimeField()

    class Meta:
        model = Match
        fields = '__all__'