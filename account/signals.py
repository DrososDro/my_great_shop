from django.db.models.signals import post_save
from django.core.mail import send_mail
from account.models import Account


def sending_activation_mail(sender, instance, created, **kwargs):
    if created:
        '''

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

        '''


post_save.connect(sending_activation_mail, sender=Account)
