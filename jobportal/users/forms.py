from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Account

ACCOUNT_TYPE_OPTIONS = [
    ('is_employee', _('Employee')),
    ('is_employer', _('Employer'))
    ]

class AccountRegisterForm(UserCreationForm):
    type = forms.CharField(label=_('User type'), widget=forms.RadioSelect(choices=ACCOUNT_TYPE_OPTIONS))

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name') # the password will be created by UserCreationForm or something like that
