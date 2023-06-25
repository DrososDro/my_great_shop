from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from account.models import Account
from account.admin import UserCreationForm
from account.forms import UpdateAccount
from account.utils import profile_img_rename

# Create your views here.


def home(request):
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

    def get_success_url(self):
        messages.success(
            self.request,
            "Your account has been created Check your email to activate it",
        )
        return super().get_success_url()


class UserProfile(UpdateView):
    model = Account
    template_name = "account/user_account.html"
    form_class = UpdateAccount

    def get_success_url(self):
        self.success_url = self.object.account_url()
        return super().get_success_url()

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        profile_img_list = self.request.FILES.getlist("upload_profile_images")
        profile_img_rename(profile_img_list, self.object)
        return redirect(self.get_success_url())
