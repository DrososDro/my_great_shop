import uuid
from account.models import MultipleImages


def profile_img_rename(images, obj):
    for img in images:
        img.name = f"{uuid.uuid4()}.{img.name.split('.')[-1]}"
        MultipleImages.objects.create(
            image_name=img,
            account=obj,
        )
