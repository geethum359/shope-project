from django.contrib.auth.forms import UserCreationForm
from shopapp .models import CustomUser
from django import forms
# from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone')