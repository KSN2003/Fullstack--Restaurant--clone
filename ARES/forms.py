# from django.forms import ModelForm

# from .models import contact

# class contact(ModelForm):
#     class Meta:
#         model = contact
#         fields = ['name', 'email', 'subject', 'message']

# for user registeration sing and sign out
from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']