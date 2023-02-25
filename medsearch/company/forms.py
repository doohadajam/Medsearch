from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.db import transaction

# This is a form for user login
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

# This is a form for creating a new company
class CompanyCreationForm(UserCreationForm, forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    name = forms.CharField(max_length=255, required=True)
    # The following line creates a field for the description of the company, with a textarea widget and a CSS class
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}))
    # The following line creates a field for the logo of the company, with a clearable file input widget and a CSS class
    logo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-input'}))

    # Add any additional fields you want to collect from the company during registration

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # This is a method that saves the new user and company to the database
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        # The following line creates a new CompanyModel instance with the user as the foreign key, and assigns the name, description, and logo from the form data
        company = CompanyModel.objects.create(
            user=user,
            name=self.cleaned_data.get('name'),
            description=self.cleaned_data.get('description'),
            logo=self.cleaned_data.get('logo')
            # Assign any additional fields from the form to the Company model
        )
        return company

    
class CompanyUpdateForm(forms.ModelForm):
        email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
        first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
        last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
        name = forms.CharField(max_length=255, required=True)
        description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}))

        class Meta:
            model = User
            fields = ('email', 'first_name', 'last_name')

        def save(self,company):
            company.user.email = self.cleaned_data.get('email')
            company.user.first_name = self.cleaned_data.get('first_name')
            company.user.last_name = self.cleaned_data.get('last_name')
            company.user.save()
            company.name = self.cleaned_data.get('name')
            company.description = self.cleaned_data.get('description')
            company.save()
            return company

