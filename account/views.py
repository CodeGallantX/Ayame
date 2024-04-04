from sqlite3 import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from Transactions.models import Transaction
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
#from .models import UserProfile, UserBankAccount, AccountData

# Create views here

'''def account_detail(request, account_number):
    # Retrieve account details based on account_number
    # Implement your logic here
    return render(request, 'account_detail.html', {'account': account_details})      '''


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('account:login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})


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