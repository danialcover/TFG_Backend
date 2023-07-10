from rest_framework import serializers

from club.models import Team, Location
from league.models import Group, GroupTeam, MatchDay
from user.models import Profile
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    match_day = serializers.PrimaryKeyRelatedField(queryset=MatchDay.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), required=False)
    group_team1 = serializers.PrimaryKeyRelatedField(queryset=GroupTeam.objects.all())
    group_team2 = serializers.PrimaryKeyRelatedField(queryset=GroupTeam.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    date = serializers.DateTimeField()

    class Meta:
        model = Match
        fields = '__all__'