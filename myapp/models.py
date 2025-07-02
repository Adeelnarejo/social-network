from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    comments_count = models.PositiveIntegerField(default=0)

    def total_likes(self):
        return self.likes.count()


def __str__(self):
    return f"{self.user.username}'s Post ({self.created_at.date()})"



class OpenHouse(models.Model):
    event_name = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    event_image = models.ImageField(upload_to='open_house_images/', null=True, blank=True)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name
