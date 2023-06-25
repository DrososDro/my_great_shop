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
