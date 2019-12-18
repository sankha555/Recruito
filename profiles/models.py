from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageFile
from django.urls import reverse
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
import requests

#Org = apps.get_model('orgs', 'Org')

sex_choices = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Rather Not Say'),]

#model for profile of a user
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE, default = 0)
    bits_id = models.CharField(max_length = 15, unique = True, default = "0000P")
    name = models.CharField(max_length = 50, default = " ")
    birthday = models.DateField(default = timezone.now)
    city = models.CharField(max_length = 20, default = " ")
    sex = models.CharField(
        max_length = 20,
        choices = sex_choices,
        default = 0,
    )

    bio = models.TextField(max_length = 100, default = " ")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    applied_orgs = models.ManyToManyField(User, blank=True, related_name='applied_orgs', default=None)
    member_orgs = models.ManyToManyField(User, blank=True, related_name='member_orgs', default=None)

    qualifier = models.IntegerField(default=0) #qualifier : Orgs - 1  Students - 0

    def get_age(self):
        return 2019 - self.birthday.year

    def profile_create_url(self):
        return reverse('create_profile', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_profile_user(self):
        return self.user

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Create your models here.
