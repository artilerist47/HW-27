from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Location
from ads.permissions import AdsCreatePermission
from ads.serializers.loc_serializer import LocSerializer


class LocatiionsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]