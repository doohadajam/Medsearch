from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

# View for registering a new company
def register_view(request):
    if request.method == 'POST':
        # If the form has been submitted, try to create a new company using the form data
        form = CompanyCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # If the form is valid, redirect to the login page
            return redirect('login')
        else:
            # If the form is not valid, print the errors to the console and redisplay the form
            print(form.errors)
    else:
        # If the request method is GET, display the form for registering a new company
        form = CompanyCreationForm()
    return render(request, 'signup.html', {'form': form})

# View for logging in to the website
def login_view(request):
    if request.method == 'POST':
        # If the form has been submitted, try to log in the user using the form data
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # If the user is authenticated, log them in and redirect to the dashboard
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('index')
            else:
                # If the user is not authenticated, display an error message and redisplay the login form
                messages.error(request, 'Invalid username or password.')
    else:
        # If the request method is GET, display the login form
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})

# View for logging out of the website
def logout_view(request):
    # Log the user out and redirect to the login page
    logout(request)
    return redirect('login')

# View for the dashboard page
def dashboard(request):
    if not request.user.is_authenticated:
        # If the user is not authenticated, redirect to the login page
        return redirect('login')
    else:
        # If the user is authenticated, display the dashboard page
        return render(request, 'index.html')

# View for adding a new medicine
def addNewMedicine(request):
    if not request.user.is_authenticated:
        # If the user is not authenticated, redirect to the login page
        return redirect('login')
    else:
        # If the user is authenticated, display the form for adding a new medicine
        return render(request, 'add-medicine.html')

# View for displaying a list of all medicines
def medicinesList(request):
    if not request.user.is_authenticated:
        # If the user is not authenticated, redirect to the login page
        return redirect('login')
    else:
        # If the user is authenticated, display the list of all medicines
        return render(request, 'medicines-list.html')


@login_required
def company_profile(request):
    # Get the company associated with the current user
    company = CompanyModel.objects.get(user=request.user)
    initial_data = {
        'email': company.user.email,
        'first_name': company.user.first_name,
        'last_name': company.user.last_name,
        'name': company.name,
        'description': company.description,
        'logo': company.logo
    }
    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(company)
            return render(request, 'company_profile.html', {'form': form , 'initial_data' :initial_data})

        else:
            print(form.errors)
    else:
        form = CompanyUpdateForm(initial_data)
    return render(request, 'company_profile.html', {'form': form , 'initial_data' :initial_data})



def logo_path(request):
    if request.user.is_authenticated:
        company = CompanyModel.objects.get(user=request.user)
        return {'logo_path': company.logo.url}
    else:
          return {'logo_path': ''}

