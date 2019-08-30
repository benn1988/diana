"""
Module for the post on the blog
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """Model for Post"""
    PERSONAL = 'personal'
    HAIRCOLOR = 'hair color'
    HAIRCUT = 'haircut'
    HAIRCARE = 'hair care'
    HAIRSTYLE = "hairstyle"
    MAKEUP = "makeup"
    categories = ((PERSONAL, 'Personal'), (HAIRSTYLE, 'Hairstyle'), (MAKEUP, 'Makeup'), (HAIRCOLOR, 'Hair Color'), (HAIRCUT, 'Haircut'), (HAIRCARE, 'Hair Care'))
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_photo = CloudinaryField('image')
    date_posted = models.DateTimeField('Posted On', default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=categories, default=HAIRSTYLE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Method for returning the post detail url for the post with specified id
        """
        return reverse('post-detail', kwargs={'pk': self.pk})
