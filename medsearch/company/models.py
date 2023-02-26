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




class Medicine(models.Model):
    class Category(models.TextChoices):
        ANTIBIOTIC = 'Antibiotic'
        ANALGESIC = 'Analgesic'
        ANTI_INFLAMMATORY = 'Anti-inflammatory'
        ANTIHISTAMINE = 'Antihistamine'
        ANTIHYPERTENSIVE = 'Antihypertensive'
        ANTIMALARIAL = 'Antimalarial'
        ANTIMICROBIAL = 'Antimicrobial'
        VITAMINS = 'Vitamins'
        HERBAL_MEDICINE = 'Herbal Medicine'
        OTHERS = 'Others'

    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHERS)
    photo = models.ImageField(upload_to='medicine_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = models.TextField()

    def __str__(self):
        return self.name
