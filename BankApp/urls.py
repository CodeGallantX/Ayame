"""
URL configuration for BankApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from base import views  # Import the views from base app
from account import urls


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.home, name='home'),
    #path('account/', infinity_views.account, name='account'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    #path('send-email/', infinity_views.send_email, name='send-email'),
    path('thank-you/', views.thank_you, name='thank_you'),
  
  #  path('buy-airtime/', infinity_views.buy_airtime, name='buy_airtime'),

    # TRANSACTIONS
    # path('transactions/', include('transactions.urls')),

    #path("process_account_action/", infinity_views.get_account_action, name='get_account_action'),
    #path("withdraw/", infinity_views.withdraw, name='withdraw'),
    #path("deposit/", infinity_views.deposit, name='deposit'),
    #path("stat_gen/", infinity_views.stat_gen, name='stat_gen'),
    #path("get_stat_gen/", infinity_views.get_transaction_action, name='get_transaction_action'),
    #path("pay_bill/", infinity_views.pay_bill, name='pay_bill'),

    # ACCOUNT URLS
    path('', include('account.urls')),
]


handler404 = 'base.views.error_404'  # Correct the handler404 to use the correct module path
