from types import CoroutineType
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from account.models import Account
import uuid


class AccountProfile(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # job_role
    # company = models.CharField(max_length=200, blank=True, null=True)
    # telephone
    # images

    # wishlist
