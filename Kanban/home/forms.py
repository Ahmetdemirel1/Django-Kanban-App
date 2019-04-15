from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from  .models import *
from django.contrib.auth.models import User







class PersonForm(forms.ModelForm):
    username = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password', "type": "password"}))




