from rest_framework import serializers

from club.models import Team
from .models import League, Group, GroupTeam, MatchDay


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'year']


class GroupSerializer(serializers.ModelSerializer):
    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all())

    class Meta:
        model = Group
        fields = '__all__'


class GroupTeamSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    num_matches_played = serializers.IntegerField(default=0, allow_null=True, required=False)
    num_wins = serializers.IntegerField(default=0, allow_null=True, required=False)
    num_draws = serializers.IntegerField(default=0, allow_null=True, required=False)
    num_losses = serializers.IntegerField(default=0, allow_null=True, required=False)
    goals_scored = serializers.IntegerField(default=0, allow_null=True, required=False)
    goals_conceded = serializers.IntegerField(default=0, allow_null=True, required=False)
    points = serializers.IntegerField(default=0, allow_null=True, required=False)
    match_outcomes = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = GroupTeam
        fields = '__all__'


class MatchDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDay
        fields = '__all__'
