from django.urls import path
from products import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("<slug:slug>", views.CategoryView.as_view(), name="category"),
]
