from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='profiles', null=True, blank=True)

    def get_image(self):
        return self.image.url if self.image else settings.STATIC_URL + 'images/profile.jpg'

