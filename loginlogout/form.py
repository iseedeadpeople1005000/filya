from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(ModelForm):
	class Meta():
		model = User
		fields = ['username', 'email', 'password']