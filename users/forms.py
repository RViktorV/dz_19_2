from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['phone_number', 'country']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['email', 'password1', 'password2']
