from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import EmailMessage, get_connection
import random
from account.models import AccountData
from Transactions.models import Transaction


def home(request):
    return render(request, 'base/homepage.html')

def error_404(request, exception):
    return render(request, 'base/404.html', status=404)

@login_required
def dashboard(request):
    balance = request.balance
    try:
        wallet = AccountData.objects.get(balance=balance)
        recent_transactions = Transaction.objects.filter(wallet=wallet).order_by('-timestamp')[:5]
    except AccountData.DoesNotExist:
        wallet = None
        recent_transactions = []

    context = {
        'wallet': wallet,
        'recent_transactions': recent_transactions,
    }
    return render(request, 'base/dashboard.html', context)



def contact(request):
    return render(request, 'base/contact.html')

def thank_you(request):
    return render(request, 'base/thank_you.html')

def blog(request):
    return render(request, "base/blog.html")

def pricing(request):
    return render(request, "base/pricing.html")

def send_email(request):  
   if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = request.POST.get("subject")  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [request.POST.get("email"), ]  
           message = request.POST.get("message")  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 
   return render(request, 'home.html')
