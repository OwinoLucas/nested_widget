from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['properties_link']

#         widgets = {' properties_link': nestedwidget()}