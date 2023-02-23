from django.db import models
from django.contrib.auth.models import User

# Define a model for a company
class CompanyModel(models.Model):
    # Define a one-to-one relationship with the built-in User model of Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add a field to store the name of the company
    name = models.CharField(max_length=255)
    # Add a field to store the description of the company
    description = models.TextField()
    # Add a field to store the logo of the company
    logo = models.ImageField(upload_to='company_logos')
    # Add any additional fields you want to collect from the company during registration

    # Define a string representation for the company object
    def __str__(self):
        return self.name
