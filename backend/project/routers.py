from rest_framework import routers
from twitter.views import TweetView

router = routers.DefaultRouter()
router.register(r"tweet", TweetView)
