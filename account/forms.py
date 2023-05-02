from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from .models import Person
# from django.db.models import Q
# from django.core.exceptions import ValidationError
# import datetime
# from django.forms.widgets import NumberInput
# from django.forms.widgets import TextInput

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ['username', 'paypal', 'country', 'bank_name', 'account_no', 'account_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = ""
        self.fields['password2'].label = "Password Confirmation"

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Person
        fields = ['old_password', 'new_password1', 'new_password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = ""
        # self.fields['password2'].label = "Password Confirmation"

class CustomRegisterFormPoster(UserChangeForm):

    class Meta:
        model = Person
        fields = ['username', 'paypal', 'country', 'bank_name', 'account_no', 'account_name']
