# In Account.urls.py
from django.urls import path
from account import views as account_views

urlpatterns = [
    # path('<str:account_number>/', account_views.account_detail, name='account_detail'), 
    path('accounts/login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    path('register/', account_views.register, name='register'),
    # Add other URLs as needed
]
