from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from .forms import AccountRegisterForm


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user-register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = _('Your user account has been created')


class UserLoginView(CreateView):
    pass
