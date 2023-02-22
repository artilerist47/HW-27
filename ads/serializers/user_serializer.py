from rest_framework import serializers

from ads.models import User


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        # many=True,  #не отображается в виде списка и по чему-то не заносится id локации в таблицу юзеров
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "role",
            "age",
            "locations",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        # many=True,  #не отображается в виде списка и по чему-то не заносится id локации в таблицу юзеров
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "role",
            "age",
            "locations",
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    # locations = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=locations.object.all(),  #&&&&&&&&&
    #     slug_field = "name"
    # )
    # author = serializers.CharField()
    # id = serializers.IntegerField(required=False)  #зачем оно нужно???

    class Meta:
        model = User
        # exclude = ["locations"]
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "role",
            "age",
            # "locations"
        ]
    #
    # def is_valid(self, *, raise_exception=False):
    #     self._locations = self.initial_data.pop("locations")
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def create(self, validated_data):
    #     user_ = User.objects.create(**validated_data)
    #     ###
    #     user_.save()
    #     return user_


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "age",
            # "locations"
        ]

    # def is_valid(self, *, raise_exception=False):
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def save(self):
    #     ad = super().save()
    #     ad.save()
    #     return ad


class UserDeleteSerializer(serializers.ModelSerializer):
    class Mete:
        model = User
        fields = "__all__"