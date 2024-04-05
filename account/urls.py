# In Account.urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('<str:account_number>/', account_views.account_detail, name='account_detail'), 
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    # Add other URLs as needed
]
