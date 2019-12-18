from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Org, OrgMember
from profiles.models import Profile

@receiver(post_save, sender=User)
def create_new_org(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Org.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_org_profile(sender, instance, **kwargs):
        instance.profile.qualifier = 0
        instance.org.qualifier = 1
        instance.profile.save()
        instance.org.save()
