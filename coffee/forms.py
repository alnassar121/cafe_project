from django import forms
from django.contrib.auth.models import User 


class UserSignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

		widgets = {
		'pasword': forms.PasswordInput(),
		}

class UserLoginForm(forms.ModelForm):
	
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())