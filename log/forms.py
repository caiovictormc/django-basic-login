from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    email = forms.CharField(label="Email", max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))
    password_again = forms.CharField(label="Repeat your password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))
