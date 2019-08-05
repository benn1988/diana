"""
Module for the post on the blog
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField


class Post(models.Model):
    """Model for Post"""
    personal = 'Personal'
    hairstyle = "Hairstyle"
    makeup = "Makeup"
    categories = ((personal, 'Personal'), (hairstyle, 'Hairstyle'), (makeup, 'Makeup'))
    title = models.CharField(max_length=50)
    content = HTMLField()
    post_photo = models.ImageField(default="default_blog.jpg", upload_to='post_photo')
    date_posted = models.DateTimeField('Posted On', default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=categories, default=hairstyle)


    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Method for returning the post detail url for the post with specified id
        """
        return reverse('post-detail', kwargs={'pk': self.pk})
