from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import User
from ads.permissions import AdsCreatePermission
from ads.serializers.user_serializer import UserListSerializer, UserDetailSerializer, UserCreateSerializer, \
    UserUpdateSerializer, UserDeleteSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        user_name = request.GET.get('username', None)
        if user_name:
            self.queryset = self.queryset.filter(
                username__icontains=user_name
            )
        loc_name = request.GET.get('first_name', None)
        if loc_name:
            self.queryset = self.queryset.filter(
                first_name__icontains=loc_name
            )
        loc_name = request.GET.get('last_name', None)
        if loc_name:
            self.queryset = self.queryset.filter(
                last_name__icontains=loc_name
            )
        loc_name = request.GET.get('role', None)
        if loc_name:
            self.queryset = self.queryset.filter(
                role__icontains=loc_name
            )
        loc_name = request.GET.get('age', None)
        if loc_name:
            self.queryset = self.queryset.filter(
                age__icontains=loc_name
            )
        loc_name = request.GET.get('locations', None)
        if loc_name:
            self.queryset = self.queryset.filter(
                locations__name__icontains=loc_name
            )

        return super().get(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]
