from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
                'password': forms.PasswordInput()
            }
        help_texts = {
            'username': "(max. 20 letters/digits/special characters)"
        }


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }