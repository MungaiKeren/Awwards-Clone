from rest_framework import serializers
from .models import Projects, Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('image', 'title', 'description', 'link', 'post_date', 'profile', 'author')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'pic', 'bio', 'contact_info')
