
from django import forms
from .models import User
from django.db import models
class RegisterForm(forms.ModelForm):
    password2 = models.CharField(max_length=255) 
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['name', 'email', 'password']
        # extra_kwargs={
        #     'password':{'write_only':True}
        # }