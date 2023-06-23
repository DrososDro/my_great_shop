from django.db.models.signals import post_save
from account.models import Account
from django.core.mail import send_mail


def sending_welcome_mail(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "{{Welcome to our company}}",
            """
Here is the message.
is is in multiple lines
or in one
k
        """,
            "drosostest@gmail.com",
            ["drosinakis.drosos1@gmail.com"],
            fail_silently=False,
        )


post_save.connect(sending_welcome_mail, sender=Account)
