# form that inheritsfrom the user creation format
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # this class give nested namespace for configurations, inherit from usercreationform
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
