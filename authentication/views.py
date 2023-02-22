from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import Profile
from authentication.serizlizers import ProfileCreateSerializer


class ProfileCreateView(CreateAPIView):
    model = Profile
    serializer_class = ProfileCreateSerializer


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)