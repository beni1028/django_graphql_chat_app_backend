from django import forms
from django.contrib.auth.forms import UserCreationForm

import hashlib
from account.models import User
import decimal, random
from datetime import datetime


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        # fields = ('email','username','is_admin','is_active','is_staff','is_superuser','is_a_supervisor','profile_image','reporting_manager','role','phone_number','emergency_contact','address','blood_group','first_name','last_name','middle_name','employee_id')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
    
    def generate_password(self):
        s=str(self['email'].value())+str(datetime.now())
        hash = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8
        print(self.cleaned_data['email'])
        # self['password1'] = hash
        return hash
