from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Role, Profile


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True, required=False)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'roles']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()

        roles = validated_data.pop('roles')
        profile = Profile.objects.create(user=user, **validated_data)
        profile.roles.set(roles)
        profile.save()

        return profile


class ProfileBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        userModel = get_user_model()
        try:
            user = userModel.objects.get(username=username)
            if user.check_password(password):
                try:
                    profile = Profile.objects.get(user=user)
                    return profile
                except Profile.DoesNotExist:
                    pass
        except userModel.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
