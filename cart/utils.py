from cart.models import Cart
from account.models import BillingAdress


def _cart_id_from_session(request):
    session = request.session
    if not session.session_key:
        session.create()
        session.set_expiry(64 * 3600)
    return session.session_key


def get_or_create_cart(request, show_created=False):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(
            cart_id=_cart_id_from_session(request)
        )
    if show_created:
        return cart, created
    return cart


def get_billint_address(request):
    billint_dict = {
        key.replace("_", " "): value
        for key, value in BillingAdress.objects.get(
            billing_address=request.user
        ).__dict__.items()
        if key not in {"_state", "id", "billing_address_id", "delivery_address_id"}
    }
    return billint_dict


def get_delivery_address(request):
    delivery_dict = {
        key.replace("_", " "): value
        for key, value in BillingAdress.objects.get(
            delivery_address=request.user
        ).__dict__.items()
        if key not in {"_state", "id", "billing_address_id", "delivery_address_id"}
    }
    return delivery_dict
