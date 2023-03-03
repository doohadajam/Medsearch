from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard view
    path('company-admin', views.dashboard, name='company-admin'),
    path('company-admin/dashboard', views.dashboard, name='dashboard'),
    # Add new medicine view
    path('company-admin/medicines',views.medicine_view,name='medicines'),
    path('company-admin/create_medicine',views.create_medicine,name='create_medicine'),
    # Login view
    path('company-admin/login',views.login_view,name="login"),
    # Register view
    path('company-admin/register',views.register_view,name="register"),
    # Logout view
    path('company-admin/logout', views.logout_view, name='logout'),
    path('company-admin/company_profile', views.company_profile, name='company_profile'),
    path('company-admin/delete_medicine/<int:pk>', views.delete_medicine, name='delete_medicine'),
    path('company-admin/update_medicine/<int:pk>', views.update_medicine, name='update_medicine'),

]



