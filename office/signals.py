from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from office.models.api import ApiKey
from office.models.profile import Profile, ProfileType


@receiver(pre_save, sender=ApiKey)
def make_api_user(sender, instance, **kwargs):
    if instance.api_user_id is None:
        password = str(uuid4())
        instance.api_user = User.objects.create(
            username=instance.api_username,
            email="",
            first_name="",
            last_name="",
            password=make_password(password),
        )
        Profile.objects.create(
            profile_type=ProfileType.COMPANY_API,
            user=instance.api_user,
            name=f"API USER: {instance.company.name} - {instance.channel}",
            company=instance.company,
        )
