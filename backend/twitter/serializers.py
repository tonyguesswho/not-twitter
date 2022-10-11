from rest_framework import routers, serializers, viewsets

from .models import Tweet


class Tweeterializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id", "name", "message", "created_at"]
