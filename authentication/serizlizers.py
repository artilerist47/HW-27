from rest_framework import serializers

from authentication.models import Profile


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        profile = super().create(validated_data)

        profile.set_password(profile.password)
        profile.save()

        return profile
