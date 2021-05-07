from django import forms
from .models import User
from django.core import validators


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'birthdate', 'roll', 'password'] 
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'birthdate': forms.widgets.DateTimeInput(attrs={"type": "date", 'class':'form-control'}),
            'roll': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

