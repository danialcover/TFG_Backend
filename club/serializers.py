from rest_framework import serializers

from .models import Team, Club, Location, Member


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name']


class TeamSerializer(serializers.ModelSerializer):
    club = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())

    class Meta:
        model = Team
        fields = ['id', 'name', 'club']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'address', 'postal_code', 'city']

class MemberSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Member
        fields = '__all__'
