from django import forms
from django.core import validators
from firstap.models import UserProfileInfo
from django.contrib.auth.models import User


class Form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    verify_pass = forms.CharField(label='enter password again')
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        verify_pass = all_clean_data['verify_pass']
        if password!=verify_pass:
            raise forms.ValidationError('Password not match')

class FormUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username","email","password")
class FormUserInfo(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("profile_picture","portfolio")