from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Photocateg(models.Model):
    """Model for Gallery Photo Category"""
    HAIRCUT = "haircut"
    HAIRCOLOR = "hair color"
    HAIRSTYLE = "hairstyle"
    MAKEUP = "makeup"
    categories = (
        (HAIRCUT, 'Haircut'),
        (HAIRSTYLE, 'Hairstyle'),
        (MAKEUP, 'Makeup'),
        (HAIRCOLOR, 'Hair Color'),
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
    photo_full = CloudinaryField('image', folder="gallery")
    photo_thumb = CloudinaryField('image', folder="gallery")
    date_uploaded = models.DateTimeField('Posted On', default=timezone.now)
    categories = models.ForeignKey(Photocateg, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
