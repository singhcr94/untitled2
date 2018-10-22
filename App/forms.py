from django import forms
from django.db import models
from .models import person

class create(forms.ModelForm):
    class Meta:
        model=person
        fields=['firstname','lastname','dob','phone','address']

