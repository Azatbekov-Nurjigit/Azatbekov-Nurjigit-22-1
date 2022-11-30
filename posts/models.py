from django.db import models

# Create your models here.


class Post_view(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)


class Hashtag_view(models.Model):
    description = models.TextField()
    image = models.ImageField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)



