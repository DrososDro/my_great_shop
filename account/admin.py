from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from account.models import Account, Permissions, MultipleImages
from django.contrib.auth.password_validation import validate_password


# Register your models here.
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Account
        fields = ["email", "username", "first_name", "last_name"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        validate_password(password1)
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.email.lower()
        user.username = user.username.lower()
        user.first_name = user.first_name.lower()
        user.last_name = user.last_name.lower()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control form-control-lg text-4"},
            )


class UserAdmin(BaseUserAdmin):
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "date_joined",
        "last_login",
    ]
    list_filter = ["is_admin", "is_active"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "User Info",
            {
                "fields": [
                    "username",
                    "first_name",
                    "last_name",
                    "telephone",
                    "id_number",
                    "tax_id_number",
                    "job_role",
                    "company",
                    "profile_image"
                ]
            },
        ),
        (
            "User Permissions",
            {
                "fields": [
                    "is_active",
                    "is_admin",
                    "is_superadmin",
                    "is_staff",
                    "permissions",
                ]
            },
        ),
        ("Login Details", {"fields": ["date_joined", "last_login"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ],
            },
        ),
    ]

    search_fields = ["email"]
    ordering = ["email", "last_login", "date_joined", "username"]
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = []


admin.site.register(Account, UserAdmin)
admin.site.register(Permissions)
admin.site.register(MultipleImages)
admin.site.unregister(Group)
