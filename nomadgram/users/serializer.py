from rest_framework import serializers

from nomadgram.images.serializers import UserProfileImageSerializer
from nomadgram.users.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    images = UserProfileImageSerializer(many=True)

    class Meta:
        model = User
        fields = ['profile_image', 'username', 'name', 'bio', 'website', 'post_count',
                  'followers_count', 'following_count', 'images']


class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'profile_image', 'username', 'name']