from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("profile/<str:pk>/", views.UserProfile.as_view(), name="profile"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path(
        "billing-address/<str:pk>/",
        views.BillingAddressView.as_view(),
        name="billing-address",
    ),
    path(
        "delivery-address/<str:pk>/",
        views.DeliveryAddressView.as_view(),
        name="delivery-address",
    ),
]
