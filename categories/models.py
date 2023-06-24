from django.db import models
import uuid

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4(),
        unique=True,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField()
