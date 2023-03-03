from django.shortcuts import render,redirect, get_object_or_404
from company.models import *
import json
from .models import Customer
import requests
import re
from .forms import CustomerRegistrationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth import logout


# View index page for the main page

def index(request):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'user-template/main.html', context)

# View for search medicines

def search_medicines(request):

    if not request.user.is_authenticated:
        if (request.session.get('search_count', 0) >= 5 ):
                return redirect('customer-register')
    payload = {'isOverlayRequired': False,
               'apikey': 'K82412945188957',
               'language': 'eng',
               }
    query = request.POST.get('q')
    medicines=[]
    try:
        image_file=request.FILES['image']
        if image_file:
            # this is the api that i use !!
            r = requests.post('https://api.ocr.space/parse/image', 
                          files={image_file.name: image_file},
                          data=payload,
                          )
            jsonResault=json.loads(r.content.decode());
            image_text_list=jsonResault['ParsedResults'][0]['ParsedText'].split(' ')
            
            clean_text = ""
            for txt in image_text_list:
                clean_text +=re.sub(r'[^A-Za-z]+', ' ', txt)

            phrases = clean_text.split(" ")
        
            for word in phrases:
                medicines = Medicine.objects.filter(Q(name__icontains=word))
                if len(medicines) > 0:
                    break
            context = {'medicines': medicines}
            return render(request, './user-template/view_medicins.html', context)

       

            # If no image was submitted, use the query parameter as the text
    except :
        if query:
                medicines = Medicine.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
                context = {'medicines': medicines}
                return render(request, './user-template/view_medicins.html', context)

   

# View for medicine detail

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    ingredients=medicine.ingredients.split(',');
    return render(request, './user-template/medicine_detail.html', {'medicine': medicine , 'ingredients':ingredients})

# View for copany details

def company_details(request, company_id):
    company = get_object_or_404(CompanyModel, id=company_id)
    return render(request, './user-template/company_details.html', {'company': company})

# View for customer register 

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_view')
        else:
            print(form.errors)
    else:
        form = CustomerRegistrationForm()
    return render(request, './user-template/registration.html', {'form': form})


# View for logging of the website

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
    else:
        form = CustomAuthenticationForm()
    return render(request, './user-template/login.html', {'form': form})

# View for logout of the website
def logout_view(request):
    logout(request)
    request.session['search_count'] = 0
    return redirect('index')




def view_medicins (request):

    medicines = Medicine.objects.all()

    return render(request,'./user-template/view_medicins.html', { 'medicines': medicines })
