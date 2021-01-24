from django.db import models
from django.contrib.auth.models import User

#   signal setup
from django.db.models.signals import post_save
from django.dispatch import receiver

#  dropdown menu to select countries
from django_countries.fields import CountryField

#   import from other apps within this project


#   Information required when creating a User Profile
class UserProfile(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE)
=======
    default_user = models.OneToOneField(User, on_delete=models.CASCADE)
>>>>>>> bab856ba43cb0ce4c8c70c410226a95cb4d4e1ee
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        #   create a new instance of Profile
        UserProfile.objects.create(user=instance)
    else:
        #   existing users: just save/adjust the profile information
        instance.userprofile.save()