from django.db import models
import uuid

from django.urls import reverse

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length=200, unique=True)
    category_slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @property
    def get_url(self):
        return reverse(
            "category",
            kwargs={"category_slug": self.category_slug},
        )
