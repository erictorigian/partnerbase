# marketing/forms.py
from django import forms
from .models import WaitlistSignup

class WaitlistSignupForm(forms.ModelForm):
    class Meta:
        model = WaitlistSignup
        fields = ['name', 'email', 'company', 'role']