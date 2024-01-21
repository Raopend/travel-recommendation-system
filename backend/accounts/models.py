import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.CharField(blank=True, max_length=255, null=True, default="https://picsum.photos/200/200")
