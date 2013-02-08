from django.db import models
from django.contrib.auth.models import User as BaseUser, UserManager
from django_extensions.db.models import ActivatorModel, TimeStampedModel, ActivatorModelManager
from django_extensions.db.fields import UUIDField


class UserProfileManager(UserManager):
    def find_user_by_email(self, email):
        try:
            return self.get_query_set().get(email=email)
        except User.DoesNotExist:
            return None


class User(BaseUser):
    objects = UserProfileManager()

    class Meta:
        proxy = True
