from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from orgs.models import Org

'''@receiver(post_save, sender=User)
def send_appl_email(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Org.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.qualifier = 1
        instance.org.qualifier = 0
        instance.profile.save()
        instance.org.save()'''
