from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        
        

    else:
        return render(request, 'account/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')
