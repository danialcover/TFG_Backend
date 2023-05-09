from rest_framework import serializers

from club.serializers import TeamSerializer
from .models import League, Group, GroupTeam


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'year']


class GroupSerializer(serializers.ModelSerializer):
    league = LeagueSerializer()

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        teams_data = validated_data.pop('teams')
        group = Group.objects.create(**validated_data)
        for team_data in teams_data:
            group.teams.add(team_data)
        group.save()
        return group

class GroupTeamSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    team = TeamSerializer()
    num_matches_played = serializers.IntegerField(default=0, allow_null=True, required=False)
    num_wins = serializers.IntegerField(default=0, allow_null=True, required=False)
    num_draws = serializers.IntegerField(default=0, allow_null=True, required=False)
    num_losses = serializers.IntegerField(default=0, allow_null=True, required=False)
    goals_scored = serializers.IntegerField(default=0, allow_null=True, required=False)
    goals_conceded = serializers.IntegerField(default=0, allow_null=True, required=False)
    points = serializers.IntegerField(default=0, allow_null=True, required=False)

    class Meta:
        model = GroupTeam
        fields = '__all__'
