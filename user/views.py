from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Profile, Role
from .serializers import ProfileSerializer, RoleSerializer, ProfileBackend

class RoleListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRefereesList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(roles__id=3)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    profile = ProfileBackend.authenticate(request, username=username, password=password)
    if profile is not None:
        profile_serializer = ProfileSerializer(profile)
        token, created = Token.objects.get_or_create(user=profile.user)
        response_data = profile_serializer.data
        response_data.update({'token': token.key})
        return Response(response_data)
    else:
        return Response({'Les Credencials introduïdes són invàlides'}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny, IsAuthenticated])
def profile_create(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def profile_delete(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        raise Http404("Profile not found")

    if request.user == profile.user or request.user.is_superuser:
        user = profile.user
        profile.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"detail": "You do not have permission to delete this profile."}, status=status.HTTP_403_FORBIDDEN)