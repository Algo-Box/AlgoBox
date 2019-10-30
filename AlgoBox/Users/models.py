from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    cc_handle = CharField(max_length = 40, blank = True)
    cf_handle = CharField(max_length = 40, blank = True)
    sp_handle = CharField(max_length = 40, blank = True)
    ac_handle = CharField(max_length = 40, blank = True)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
