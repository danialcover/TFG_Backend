from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class ProfileListByRole(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        role_id = self.kwargs['role_id']
        return Profile.objects.filter(roles__id=role_id)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def profile_create(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
