from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)
    hashtags = models.ManyToManyField('Hashtag', related_name='posts')

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    description = models.TextField()
    image = models.ImageField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.description


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.author.username}_{self.text}'
