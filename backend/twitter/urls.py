from django.urls import path

from .views import TweetView
from django.urls import include, path

urlpatterns = [
    path("api/tweet/", TweetView.as_view()),
]
