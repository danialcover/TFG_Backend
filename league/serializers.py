from rest_framework import serializers

from club.serializers import TeamSerializer
from .models import League, Group


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'year']


class GroupSerializer(serializers.ModelSerializer):
    league = LeagueSerializer(read_only=True)
    teams = TeamSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = '__all__'
