from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    groups = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'groups']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
