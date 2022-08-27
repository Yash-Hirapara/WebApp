from dataclasses import fields
from django import forms
from .models import contact,signup_master,basket

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields='__all__'


class signup_masterForm(forms.ModelForm):
    class Meta:
        model = signup_master
        fields='__all__'

class basketForm(forms.ModelForm):
    class Meta:
        model = basket
        fields='__all__'