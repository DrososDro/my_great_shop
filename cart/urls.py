from django.urls import path
from cart import views


urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path(
        "update-produt/<str:pk>/<str:action>/",
        views.UpdateProductQuantiry.as_view(),
        name="update-produt",
    ),
]
