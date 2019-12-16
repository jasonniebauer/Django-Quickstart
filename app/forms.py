from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        # Specify the model we want this form to interact with
        model = CustomUser
        # Fields we want shown on the form and in what order
        # Password1 and password 2 are shown by default
        fields = (
            'username',
            'email',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        # Specify the model we want this form to interact with
        model = CustomUser
        # Fields we want shown on the form and in what order
        fields = (
            'username',
            'email',
        )
