from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()

class CommentForm(ModelForm):
	class Meta():
		model = models.Comment
		fields = ["Comment_text"]
		widgets = {
			'Comment_text': Textarea(attrs={
				'id': 'comment_text',
				'rows': 4,
				'cols': 100,
				"maxlength": 1000,
				'required': True,
				'placeholder': 'Добавить комментарий'})}

class UserForm(ModelForm):
	class Meta():
		model = User
		fields = ['username', 'email', 'password']