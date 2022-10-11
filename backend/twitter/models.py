from django.db import models


class Tweet(models.Model):
    "Model for tweet message"
    name = models.CharField(max_length=50)
    message = models.TextField(blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} by {self.name}"
