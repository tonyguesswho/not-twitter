from django.test import TestCase
from twitter.models import Tweet


def sample_message():
    """Creare a sample message"""

    return Tweet.objects.create(name="name", message="message")


class ModelTests(TestCase):
    def test_category_str(self):
        """Test create message string representation"""
        message = Tweet.objects.create(name="name", message="message")
        self.assertEqual(str(message), f"{message.message} by {message.name}")
