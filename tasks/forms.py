#modificamos/añadimos campos al form dado por django
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import fields
from .models import Tasks

class createTask(forms.ModelForm):
    user = User
    limit_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type':'date',
            'data-target': '#id_limit_date'
        })
    )

    class Meta:
        model = Tasks
        fields = ['title', 'subtitle', 'limit_date', 'description', 'state']