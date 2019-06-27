from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    '''create the profile model'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        '''updating the save method to be able to save the picture to the profile'''
        super().save()

        img = Image.open(self.image.path)
        # crop the image size
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            width, height = img.size
        # make the image ratio square
            if img.width < 300:
                left = 0
                top = (height - width) / 2
                right = width
                bottom = width + top
                img = img.crop((left, top, right, bottom))
            width, height = img.size
            if img.height < 300:
                img = img.crop(((width-height)/2, 0, height +(width-height)/2, height))
            img.save(self.image.path)
