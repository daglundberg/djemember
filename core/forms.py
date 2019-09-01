from django import forms
from django.forms import NumberInput, TextInput, Select, DateInput, EmailInput, PasswordInput
from .models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'connection_verbose', 'connection_short', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'class': "input"}),
            'firs_name': TextInput(attrs={'class': "input"}),
            'email': EmailInput(attrs={'class': "input"}),
            'password1': PasswordInput(attrs={'class': "input"}),
            'password2': PasswordInput(attrs={'class': "input"}),
        }
