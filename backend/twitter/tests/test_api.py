from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from twitter.models import Tweet
from twitter.serializers import Tweeterializer

MESSAGE_URL = reverse("tweet:tweet-list")


def sample_message(name="place", message="message"):
    """Create and return a sample message"""
    return Tweet.objects.create(name=name, message=message)


class MessageApiTests(TestCase):
    """test messsage api"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_messages(self):
        """Test retreiving messages"""
        sample_message()
        sample_message(name="people", message="another message")
        res = self.client.get(MESSAGE_URL)
        messages = Tweet.objects.all()
        serializer = Tweeterializer(messages, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(len(res.data), len(serializer.data))
        self.assertEqual(res.data, serializer.data)

    def test_create_message(self):
        """Test creating a message"""
        payload = {"name": "Tony", "message": "my tweet"}
        res = self.client.post(MESSAGE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        message = Tweet.objects.get(id=res.data["id"])
        serializer = Tweeterializer(message)
        self.assertEqual(serializer.data["name"], payload["name"])
        self.assertEqual(serializer.data["message"], payload["message"])

    def test_create_message_with_invalid_details_fails(self):
        """Test creating a message with invalid details"""
        res = self.client.post(MESSAGE_URL, {})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        data = res.json()
        self.assertEqual(data["message"][0], "This field is required.")
        self.assertEqual(data["name"][0], "This field is required.")

    def test_create_message_with_invalid_length_fails(self):
        """Test creating a message with invalid details"""
        res = self.client.post(
            MESSAGE_URL, {"name": "tony", "message": "testmessage" * 100}
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        data = res.json()
        self.assertEqual(
            data["message"][0], "Ensure this field has no more than 50 characters."
        )
