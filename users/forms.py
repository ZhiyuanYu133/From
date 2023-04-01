from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import AuthUser
from django.utils.translation import gettext_lazy as _

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['displayName', 'profileImage', 'github', 'url']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='GitHub ID')
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ["profileImage", "username", "password", "email", "displayName"]
