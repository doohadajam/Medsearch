from django.contrib import admin
from .models import *

# Register your models here.
# class MyModelAdmin(admin.ModelAdmin):
#     # Define customizations here, such as list_display, list_filter, search_fields, etc.
#     list_display = ('name', 'description', 'created_at')

admin.site.register(CompanyModel)
admin.site.register(Medicine)