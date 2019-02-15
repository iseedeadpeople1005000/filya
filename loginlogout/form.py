from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class user_form(forms.Form):
    username = forms.CharField(
        max_length=20,
		min_length=6,
		required = True)
    email = forms.CharField(
		required = None)
    password = forms.CharField(
        max_length=20,
		min_length=6,
		required = True)