from cart.models import Cart


def _cart_id_from_session(request):
    session = request.session
    if not session.session_key:
        session.create()
        session.set_expiry(64 * 3600)
    return session.session_key


def create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(
            cart_id=_cart_id_from_session(request)
        )
    return cart
