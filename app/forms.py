from django import forms
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','password']
        widgets={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['Name','PhoneNo']
        widgets={'password':forms.PasswordInput}