from django.forms import TextInput, EmailInput, PasswordInput
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'connection_short', 'connection_verbose', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'class': "input"}),
            'firs_name': TextInput(attrs={'class': "input"}),
            'email': EmailInput(attrs={'class': "input"}),
            'password1': PasswordInput(attrs={'class': "input"}),
            'password2': PasswordInput(attrs={'class': "input"}),
        }
