from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class orderForm(ModelForm):
    class Meta:
        model=order
        fields= '__all__'

class customerForm(ModelForm):
    class Meta:
        model=customer
        fields=['name','phone', 'email']

class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2']


""" from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path)) """

""" accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete'] """