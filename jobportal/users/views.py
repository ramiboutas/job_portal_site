from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import AccountRegisterForm, UserUpdateForm
from .models import Profile

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

@method_decorator(login_required(login_url='users/login'), name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = UserUpdateForm
    success_message = _('You updated your profile')
    template_name = 'users/user-update.html'

    def form_valid(self):
        form.instance.user = self.request.user
        return super(UserUpdateForm, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserUpdateForm, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users:update_profile', kwargs={'pk': self.object.pk})
