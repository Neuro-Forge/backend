from django import forms
from . import models

class registerFrom(forms.ModelForm):
     class Meta:
         model = models.register
         fields = ['username', 'email', 'password']
         