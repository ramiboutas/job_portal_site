from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from .forms import AccountRegisterForm


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user-register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = _('Your user account has been created')

    def form_valid(self, form):
        user = form.save(commit=False)
        user_type = form.cleaned_data['type']

        if user_type == 'is_employee':
            user.is_employee = True
        elif user_type == 'is_employer':
            user.is_employer = True

        user.save()
        return  redirect(self.success_url)

class UserLoginView(LoginView):
    template_name = 'users/user-login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/user-login.html'
