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

    # def is_valid(self, *, raise_exception=False):
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def save(self):
    #     ad = super().save()
    #     ad.save()
    #     return ad


class AdDeleteSerializer(serializers.ModelSerializer):
    class Mete:
        model = Ad
        fields = "__all__"