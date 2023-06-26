from django.db.models.signals import post_save
from account.models import BillingAdress, Account


def create_billing_and_delivery_addresses(sender, instance, created, **kwargs):
    if created:
        # dict contains the values
        instance_attrs = {
            k: v
            for k, v in instance.__dict__.items()
            if k in BillingAdress().__dict__ and k not in ["id", "_state"]
        }
        # delivery_address
        delivery_address = BillingAdress.objects.create(
            delivery_address=instance, **instance_attrs
        )
        # billing_adress
        billing_adress = BillingAdress.objects.create(
            billing_address=instance, **instance_attrs
        )


post_save.connect(create_billing_and_delivery_addresses, sender=Account)
