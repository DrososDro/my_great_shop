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

    def save(self, *args, **kwargs):
        self.image_name = f"{uuid.uuid4()}.{self.image_name.split(('.')[-1])}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.image_name

    def image_url(self):
        return self.image_name.url or ""
