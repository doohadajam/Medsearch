from django import forms
from django.contrib.auth.forms import UserCreationForm, password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.forms import AuthenticationForm


class CustomerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput(attrs={'class': 'form-control'}), strip=False, help_text=_("Enter the same password as before, for verification."))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user, phone_number=self.cleaned_data['phone_number'], address=self.cleaned_data['address'])
        return customer

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))