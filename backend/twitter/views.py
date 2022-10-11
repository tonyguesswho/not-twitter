from rest_framework import generics
from twitter.serializers import Tweeterializer

from .models import Tweet


# Create your views here.
class TweetView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = Tweeterializer
