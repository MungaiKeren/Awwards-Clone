from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'url', 'image', 'title', 'description', 'link', 'post_date', 'profile', 'author')
