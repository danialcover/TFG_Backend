from rest_framework import serializers

from club.serializers import TeamSerializer
from .models import League, Group, Team


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'year']


class GroupSerializer(serializers.ModelSerializer):
    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all())
    teams = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), many=True)

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
