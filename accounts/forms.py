from django import forms
from .models import Account
from django.contrib.auth.models import User 

# Create your forms here.
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        style = { 
            'class': 'form-control',
            'required': True 
        }
        widgets = {
            'username': forms.TextInput(attrs=style),
            'password': forms.PasswordInput(attrs=style),
            'email': forms.EmailInput(attrs=style),
        }


class AccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['portfolio', 'profile_pic']
        style = { 
            'class': 'form-control',
            'required': False 
        }
        widgets = { 
            'portfolio': forms.URLInput(attrs=style),
        }