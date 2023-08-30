import os
import random

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    @staticmethod
    def send_email_func(email_user):
        send_mail(
            subject='Поздравляю',
            message='Welcome',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_user],
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.EMAIL_HOST_PASSWORD
        )

    def form_valid(self, form):
        new_user = form.save()
        self.send_email_func(new_user.email)

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
