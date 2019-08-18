from django.db import models
from django.utils import timezone


class Photocateg(models.Model):
    """Model for Gallery Photo Category"""
    HAIRCOLOR = "hair color"
    HAIRSTYLE = "hairstyle"
    MAKEUP = "makeup"
    categories = (
        (HAIRSTYLE, 'Hairstyle'),
        (MAKEUP, 'Makeup'),
        (HAIRCOLOR, 'Hair Color')
        )
    category = models.CharField(max_length=10, choices=categories, default=HAIRSTYLE)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name="Photo Category"
        verbose_name_plural="Photo Categories"


class Photo(models.Model):
    """Model for Gallery Photo"""
    title = models.CharField(max_length=50)
    photo_full = models.ImageField(default="default-blog.jpg", upload_to='gallery/')
    photo_thumbnail = models.ImageField(default="default-blog.jpg", upload_to='gallery/thumbnails')
    date_uploaded = models.DateTimeField('Posted On', default=timezone.now)
    categories = models.ForeignKey(Photocateg, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
