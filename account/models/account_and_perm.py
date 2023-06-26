from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

from django.urls import reverse


# Create your models here.
class MyUserManager(BaseUserManager):
    """Create and saves an Account with the fields"""

    def create_user(
        self,
        email,
        username,
        first_name,
        last_name,
        password=None,
    ):
        """create a user for the command line"""
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")

        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        account = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(
        self,
        email,
        username,
        first_name,
        last_name,
        password=None,
    ):
        """create super user from the command line"""
        account = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        account.set_password(password)
        account.is_staff = True
        account.is_active = True
        account.is_admin = True
        account.is_superadmin = True
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    """
    A custom User class for authentication with email or with
    user name this will be later
    """

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    permissions = models.ManyToManyField("Permissions", blank=True)

    # fields needed
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # general user settings
    receive_newsletters = models.BooleanField(default=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    id_number = models.CharField(max_length=200, null=True, blank=True)
    job_role = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    tax_id_number = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.CharField(max_length=200, null=True, blank=True)

    # here is creations of the account and the modified date
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the apps ?"
        # Simplest possible answer: Yes, always
        return True

    def full_name(self):
        """return full name as Title"""
        return f"{self.first_name} {self.last_name}".title()

    def set_profile_image(self):
        profiles = self.multipleimages_set.all()

        return [(p_i.image_url(), p_i.image_name) for p_i in profiles]

    def account_url(self):
        return reverse("profile", kwargs={"pk": self.id})

    def billing_url(self):
        return reverse(
            "billing-address", kwargs={"pk": self.billing_address.all()[0].id}
        )

    def delivery_url(self):
        return reverse(
            "delivery-address", kwargs={"pk": self.delivery_address.all()[0].id}
        )


class Permissions(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Permissions"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)
