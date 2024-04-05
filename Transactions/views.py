from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .models import Transaction
from account.models import AccountData
from .forms import TransactionForm, TransferForm, WithdrawForm, DepositForm
from django.contrib import messages


# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-timestamp')[:5]
    return render(request, 'base/dashboard.html', {'transactions':transactions})
    
def make_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'base/make_transaction.html', {'form': form})

def deposit(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deposit successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'base/dashboard.html', {'form': form})

def withdrawal(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Withdrawal successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'base/dashboard.html', {'form': form})

# Similarly, implement views for other transaction operations like transfer, payment, etc.

def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            # Process the form data and perform the transfer operation
            user_account = form.cleaned_data['user_account']
            recipient_account = form.cleaned_data['recipient_account']
            amount = form.cleaned_data['amount']
            recipient_bank_name = form.cleaned_data['recipient_bank_name']
            
            # Assuming you have the sender and recipient objects based on their account numbers
            sender_wallet = AccountData.objects.get(account_number=user_account)
            recipient_wallet = AccountData.objects.get(account_number=recipient_account)

            # Check if sender has enough balance
            if sender_wallet.balance >= amount:
                # Deduct amount from sender's wallet
                sender_wallet.balance -= amount
                sender_wallet.save()

                # Add amount to recipient's wallet
                recipient_wallet.balance += amount
                recipient_wallet.save()

                # Record the transaction
                # Assuming your Transaction model has appropriate fields to record this transaction
                # You can adjust this part based on your Transaction model structure
                Transaction.objects.create(sender=sender_wallet.user, recipient=recipient_wallet.user, amount=amount, trans_type='transfer')

                messages.success(request, 'Transfer successful!')
                return redirect('dashboard')  # Redirect to dashboard page after successful transfer
            else:
                messages.error(request, 'Insufficient balance.')
    else:
        form = TransferForm()
    
    return render(request, 'base/dashboard.html', {'form': form})


def payment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Withdrawal successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'base/dashboard', {'form': form})

# Similarly, implement views for other transaction operations like transfer, payment, etc.
