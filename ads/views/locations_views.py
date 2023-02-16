from rest_framework.viewsets import ModelViewSet

from ads.models import Location
from ads.serializers.loc_serializer import LocSerializer


class LocatiionsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocSerializer