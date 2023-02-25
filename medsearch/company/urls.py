from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard view
    path('', views.dashboard, name='index'),
    # Add new medicine view
    path('add-new-medicine',views.addNewMedicine,name='add_new_medicine'),
    # Medicines list view
    path('medicines-list',views.medicinesList,name="medicines_list"),
    # Login view
    path('login',views.login_view,name="login"),
    # Register view
    path('register',views.register_view,name="register"),
    # Logout view
    path('logout', views.logout_view, name='logout'),
    path('company_profile', views.company_profile, name='company_profile'),

]



