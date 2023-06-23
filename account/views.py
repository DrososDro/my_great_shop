from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from account.models import Account
from account.admin import UserCreationForm

# Create your views here.


def home(request):
    messages.success(request, "hello drosos")
    messages.info(request, "hello drosos")
    messages.warning(request, "hello drosos")
    messages.error(request, "error")
    return render(request, "base.html")


class Login(LoginView):
    model = Account
    template_name = "account/login_register.html"
    extra_context = {"login": True}
    next_page = reverse_lazy("home")


class Logout(LogoutView):
    next_page = reverse_lazy("home")


class Register(CreateView):
    model = Account
    template_name = "account/login_register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
