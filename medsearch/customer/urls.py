from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # index view
    path('', views.index, name='index'),
    path('/search/medicines/', views.search_medicines, name='search_medicines'),
    path('/medicines/medicine_detail/<int:medicine_id>', views.medicine_detail, name='medicine_detail'),
    path('company-details/<int:company_id>/', views.company_details, name='company_details'),
    path('register/', views.customer_register, name='customer-register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout-user'),
    path('view_medicins/', views.view_medicins, name='view_medicins'),

]


