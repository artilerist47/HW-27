from rest_framework import serializers

from ads.models import Location


class LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
