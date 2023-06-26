from django.db import models
from account.models import Account
import uuid


class MultipleImages(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    image_name = models.FileField(
        unique=True,
        upload_to="account_images",
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image_name)

    def image_url(self):
        return self.image_name.url or ""


class BillingAdress(models.Model):
    billing_address = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name="billing_address",
        null=True,
        blank=True,
    )
    delivery_address = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="delivery_address",
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
    )
    company = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(blank=True, max_length=20)
    address_line_1 = models.CharField(max_length=100, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, null=True)
    telephone = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    comment = models.TextField(blank=True, null=True)
