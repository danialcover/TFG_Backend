from rest_framework import serializers

from club.models import Team, Location
from league.models import Group
from user.models import Profile
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), required=False)
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    date = serializers.DateTimeField()

    class Meta:
        model = Match
        fields = '__all__'