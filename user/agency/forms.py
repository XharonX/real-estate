from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from ..models import User, Agency, City
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "box", "placeholder": _("enter password"), "autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"class": "box", "placeholder": _("confirm passwords"), "autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address', 'location']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'box',
                'placeholder': 'username',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'box',
                'placeholder': 'email address',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'box',
                'placeholder': _('first name'),
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'box',
                'placeholder': _('last name'),
            }),
            'phone': forms.TextInput(attrs={
                'class': 'box initial',
                'type': 'tel',
                'placeholder': _('phone number')
            }),
            'location': forms.Select(choices=("", "Enter your location"), attrs={
                'class': 'box initial',
                'placeholder': _('Enter your city/ state '),
                'required': True
            }),
            'address': forms.TextInput(attrs={
                'class': 'box auto',
                'placeholder': _('Enter your address'),
            }),

            'password1': forms.PasswordInput(attrs={
                'class': 'box',
                'placeholder': _('Enter your password'),
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'box',
                'placeholder': _('Confirm your password'),
            }),

        }

    @transaction.atomic
    def save(self, commit=False):
        user = super().save(commit=False)
        user.is_agency = True
        user.user_type = 2
        user.save()
        return user
