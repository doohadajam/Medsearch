from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard view
    path('', views.dashboard, name='index'),
    # Add new medicine view
    path('medicines',views.medicine_view,name='medicine_view'),
    path('create_medicine',views.create_medicine,name='create_medicine'),
    # Login view
    path('login',views.login_view,name="login"),
    # Register view
    path('register',views.register_view,name="register"),
    # Logout view
    path('logout', views.logout_view, name='logout'),
    path('company_profile', views.company_profile, name='company_profile'),
    path('delete_medicine/<int:pk>', views.delete_medicine, name='delete_medicine'),
    path('update_medicine/<int:pk>', views.update_medicine, name='update_medicine'),

]



