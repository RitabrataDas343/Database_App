from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'birthdate', 'roll', 'password','state', 'district'] 
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'birthdate': forms.widgets.DateTimeInput(attrs={"type": "date", 'class':'form-control'}),
            'roll': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'state': forms.widgets.Select(attrs={'class':'form-control'}),
            'district': forms.widgets.Select(attrs={'class':'form-control'}),
        }

