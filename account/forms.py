from django import forms
from account.models import Account


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
