from rest_framework import serializers

from ads.models import Category


class CatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CatDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
