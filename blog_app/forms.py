from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    pass


class RegistrationForm(UserCreationForm):
    pass

