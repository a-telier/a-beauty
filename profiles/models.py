from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product

from django_countries.fields import CountryField


class UserProfile(models.Model):
    #   only one user per profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #   default information we want to store
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


#   Create a user profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    # Existing users: just save the profile
    instance.userprofile.save()


