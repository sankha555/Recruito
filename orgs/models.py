from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageFile
from django.urls import reverse
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
import requests


type_choices = [('CLUB', 'Club'), ('DEPARTMENT', 'Department'), ('DEPT_ASSOC', 'Departmental Association'),
                ('CULT_ASSOC', 'Cultural Association')]

class Org(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length = 50, default = " ")
    type = models.CharField(
        max_length = 30,
        choices = type_choices,
        default = 0,
    )

    about = models.TextField(max_length = 100, default = " ")
    logo = models.ImageField(default='bits.jpg', upload_to='logos')
    members = models.ManyToManyField(User, blank = True, related_name = 'org_members')
    applicants = models.ManyToManyField(User, blank = True, related_name = 'org_applics')

    def org_create_url(self):
        return reverse('create_org_profile', kwargs={'pk': self.pk})

    def get_org_superuser(self):
        return self.user

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)

        if img.height>300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class OrgMember(models.Model):
    member = models.ForeignKey(User, on_delete = models.CASCADE, default = 0)
    designation = models.CharField(max_length = 20, default = "Junior Member")
    joined_on = models.DateField(default = timezone.now)
    status = models.IntegerField(default = 1) #member status: 0 - left , 1 - active

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# Create your models here.
