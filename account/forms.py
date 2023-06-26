from django import forms
from account.models import Account, BillingAdress


class UpdateAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

        exclude = [
            "password",
            "is_admin",
            "is_superadmin",
            "is_staff",
            "is_active",
            "permissions",
        ]

    def __init__(self, *args, **kwargs):
        super(UpdateAccount, self).__init__(*args, **kwargs)

        self.fields["profile_image"] = forms.ChoiceField(
            choices=self.instance.set_profile_image(),
            required=False,
        )
        for name, field in self.fields.items():
            if name == "receive_newsletters":
                continue
            field.widget.attrs.update(
                {
                    "class": "form-control text-3 h-auto py-2",
                }
            )


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAdress
        fields = "__all__"
        exclude = ["delivery_address"]

    def __init__(self, *args, **kwargs):
        super(BillingAddressForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control text-3 h-auto py-2",
                }
            )


class DeliveyAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAdress
        fields = "__all__"
        exclude = ["billing_address"]

    def __init__(self, *args, **kwargs):
        super(DeliveyAddressForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control text-3 h-auto py-2",
                }
            )
