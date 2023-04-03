from django import forms
from django.forms import ValidationError
from .models import User


def userValid(data):
    if "admin" in data:
        raise ValidationError("username can't be admin")
    else:
        return data


class UserValid:
    def __init__(self, message):
        self.message = message

    def __call__(self, data):
        if "admin" in data:
            raise ValidationError(self.message)
        else:
            return data


class UserForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3)
    password = forms.CharField(max_length=32, min_length=6)
    password_confirm = forms.CharField(max_length=32, min_length=6)

    # check data
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if "admin" in username:
            raise ValidationError("username can't be admin")
        elif User.objects.filter(username=username):
            raise ValidationError("username had used")
        else:
            return username
