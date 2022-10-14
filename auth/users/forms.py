
from django import forms
#from .models import User
from django.contrib.auth.models import User
from django.db import models
# class RegisterForm(forms.ModelForm):
#     password2 = models.CharField(max_length=255) 
#     class Meta:
#         model = User
#         #fields = '__all__'
#         fields = ['name', 'email', 'password']
#         # extra_kwargs={
#         #     'password':{'write_only':True}
#         # }

from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user