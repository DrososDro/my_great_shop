from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    get_current_site,
    urlsafe_base64_decode,
)
from django.contrib.auth.forms import (
    default_token_generator,
    force_bytes,
    urlsafe_base64_encode,
)
from django.views.generic import CreateView, UpdateView
from account.models import Account, Permissions, BillingAdress
from account.admin import UserCreationForm
from account.forms import UpdateAccount, BillingAddressForm, DeliveyAddressForm
from account.utils import profile_img_rename
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    # return render(request, "products/3_items_view.html")
    return render(request, "products/shop.html")


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
        current_site = get_current_site(self.request)
        mail_subject = "Please activate your account"
        message = render_to_string(
            "account/activation_mail.html",
            {
                "user": self.object.full_name(),
                "domain": current_site,
                "uid": urlsafe_base64_encode(force_bytes(self.object.pk)),
                "token": default_token_generator.make_token(self.object),
            },
        )

        to_email = self.object.email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        return super().get_success_url()


class UserProfile(UpdateView):
    model = Account
    template_name = "account/user_account.html"
    form_class = UpdateAccount

    def get_success_url(self):
        self.success_url = self.object.account_url()
        messages.success(
            self.request,
            "You successfully update your personal informations",
        )
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = self.request.user.account_url()
        return context

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        profile_img_list = self.request.FILES.getlist("upload_profile_images")
        profile_img_rename(profile_img_list, self.object)
        return redirect(self.get_success_url())


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        permission = Permissions.objects.get(name="customer")
        user.permissions.add(permission)

        user.save()
        messages.success(
            request,
            "Congratulations! Your Account is activated!",
        )
        return redirect("login")
    else:
        messages.error(request, "Invalid activation link")
        return redirect("register")


class BillingAddressView(UpdateView):
    model = BillingAdress
    template_name = "account/user_account.html"
    form_class = BillingAddressForm

    def get_success_url(self):
        self.success_url = self.request.user.billing_url()
        messages.success(
            self.request,
            "You successfully update your billing info",
        )
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = self.request.user.billing_url()
        return context


class DeliveryAddressView(UpdateView):
    model = BillingAdress
    template_name = "account/user_account.html"
    form_class = DeliveyAddressForm

    def get_success_url(self):
        self.success_url = self.request.user.delivery_url()
        messages.success(
            self.request,
            "You successfully update your billing info",
        )
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = self.request.user.delivery_url()
        return context
