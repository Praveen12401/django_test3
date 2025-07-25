from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            print('form save')
            form.save() 
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/register.html', {'form': form})

@login_required
def customer_home(request):
    return render(request, 'customer/home.html')

@login_required
def customer_orders(request):
    # Implement order retrieval logic here
    return render(request, 'customer/orders.html')

def handelLogout(request):
    logout(request)
    # messages.success(request, "Successfully logged out")
    return redirect('Home')