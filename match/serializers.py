from rest_framework import serializers

from .models import Match
from club.models import Team, Location
from user.models import Profile
from league.models import Group


class MatchSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), allow_null=True, required=False)
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

    class Meta:
        model = Match
        fields = '__all__'