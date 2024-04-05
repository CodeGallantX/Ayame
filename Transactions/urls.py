from django.urls import path
from .views import *

urlpatterns = [
    # path('<str:account_number>/', account_views.account_detail, name='account_detail'), 
    path('#deposit/', deposit, name='deposit'),
    path('#transfer/', transfer_funds, name='transfer'),
    path('#withdraw/', withdrawal, name='withdraw'),
    path('#transaction_opt/', make_transaction, name='transaction_opt'),
    # Add other URLs as needed
]
