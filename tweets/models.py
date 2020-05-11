from django.db import models
from django.conf import settings
import random

# Create your models here.

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #many users can have many tweets, delete all tweets from user
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #want user to delete tweets themselves, retweets say tweet was deleted
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def is_retweet(self):
        return self.parent != None

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "content": self.content,
    #         "likes": random.randint(0,200)
    #     }

    # def __str__(self):
    #     return self.content #display the msg content string in admin display

    class Meta:
        ordering = ['-id']
    