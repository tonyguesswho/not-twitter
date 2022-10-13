from rest_framework import generics, mixins, viewsets
from twitter.serializers import Tweeterializer

from .models import Tweet


# Create your views here.
class TweetView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Tweet.objects.all()
    serializer_class = Tweeterializer

    def get_queryset(self):
        return self.queryset.order_by("-created_at", "name")
