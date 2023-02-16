from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Ad
        fields = [
            "id",
            "name",
            "author_id",
            "author",
            "price",
            "description",
            "is_published",
            "category_id",
            "image"
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Ad
        fields = [
            "id",
            "name",
            "author_id",
            "author",
            "price",
            "description",
            "is_published",
            "category_id",
            "image"
        ]


class AdCreateSerializer(serializers.ModelSerializer):
    # author = serializers.CharField()
    # category
    id = serializers.IntegerField(required=False)  #зачем оно нужно???

    class Meta:
        model = Ad
        # fields = [
        #     "name",
        #     "author",
        #     "price",
        #     "description",
        #     "address",
        #     "is_published"
        # ]
        # fields = "__all__"
        exclude = ["image", "author"]


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    author_id = serializers.IntegerField(required=False)
    price = serializers.FloatField(required=False)
    description = serializers.CharField(required=False)
    is_published = serializers.BooleanField(required=False)

    class Meta:
        model = Ad
        fields = [
            "id",
            "name",
            "author_id",
            "price",
            "description",
            "is_published"
        ]


class AdDeleteSerializer(serializers.ModelSerializer):
    class Mete:
        model = Ad
        fields = "__all__"