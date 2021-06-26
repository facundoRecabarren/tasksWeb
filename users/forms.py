#modificamos/añadimos campos al form dado por django
from django.db import models
from users.models import Usuarios
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class ProfileForm(forms.ModelForm):
    job = forms.Textarea()
    description = forms.Textarea()

    #especificamos el modelo con el que va a interactuar el formulario
    class Meta:
        model = Usuarios
        fields = ['job','description']



class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['job', 'description', 'image']