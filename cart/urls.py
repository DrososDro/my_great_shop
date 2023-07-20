from django.urls import path
from cart import views


urlpatterns = [
    path("cart", views.CartView.as_view(), name="cart"),
]
