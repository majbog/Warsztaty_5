from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    image = models.ImageField(null=True)
    date = models.DateField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField()
    reference = models.ForeignKey(Message, on_delete=models.CASCADE)


class Following(models.Model):
    follower = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed_user")


class Like(models.Model):
    who_likes = models.ForeignKey(User, on_delete=models.CASCADE)
    what_likes = models.ForeignKey(Message, on_delete=models.CASCADE)



