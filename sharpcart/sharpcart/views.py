from django.shortcuts import render,redirect
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request,'login.html')


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Home')