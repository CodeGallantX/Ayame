from django.forms import forms
from .models import Transaction
from account.models import AccountData

class TransactionForm(forms.ModelForm):
    ACCOUNT_CHOICES= (
        ('savings':'Savings',
        'current':'Current'),
    )

    account = forms.ChoiceField(choices = ACCOUNT_CHOICES, label="Account Type: ")

    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'trans_type', 'description']
        
class TransferForm(forms.Form):
    user_account = forms.IntegerField(label="Your Account Number")
    recipient_account = forms.CharField(label="Recipient Account Number")
    amount = forms.DecimalField(label="Amount")
    recipient_bank_name = forms.ChoiceField(choices=[], required=True)  # Add the new field

    def __init__(self, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        # Populate the choices for the recipient_bank_name field
        # You can replace this static example with dynamic data from your database
        bank_choices = [
    ('Access Bank', 'Access Bank'),
    ('Zenith Bank', 'Zenith Bank'),
    ('Guaranty Trust Bank (GTBank)', 'Guaranty Trust Bank (GTBank)'),
    ('First Bank of Nigeria', 'First Bank of Nigeria'),
    ('United Bank for Africa (UBA)', 'United Bank for Africa (UBA)'),
    ('Ecobank Nigeria', 'Ecobank Nigeria'),
    ('Fidelity Bank Nigeria', 'Fidelity Bank Nigeria'),
    ('Union Bank of Nigeria', 'Union Bank of Nigeria'),
    ('Stanbic IBTC Bank', 'Stanbic IBTC Bank'),
    ('Sterling Bank', 'Sterling Bank'),
    ('Citibank Nigeria', 'Citibank Nigeria'),
    ('Wema Bank', 'Wema Bank'),
    ('Heritage Bank', 'Heritage Bank'),
    ('Keystone Bank', 'Keystone Bank'),
    ('Polaris Bank', 'Polaris Bank'),
    ('LAPO Microfinance Bank', 'LAPO Microfinance Bank'),
    ('AB Microfinance Bank Nigeria', 'AB Microfinance Bank Nigeria'),
    ('NPF Microfinance Bank', 'NPF Microfinance Bank'),
    ('Accion Microfinance Bank', 'Accion Microfinance Bank'),
    ('Fortis Microfinance Bank', 'Fortis Microfinance Bank'),
    ('FINCA Microfinance Bank', 'FINCA Microfinance Bank'),
    ('HASAL Microfinance Bank', 'HASAL Microfinance Bank'),
    ('Grooming Microfinance Bank', 'Grooming Microfinance Bank'),
    ('Page Microfinance Bank', 'Page Microfinance Bank'),
    ('Mainstreet Microfinance Bank', 'Mainstreet Microfinance Bank'),
    ('Moniepoint', 'Moniepoint'),
    ('Paga', 'Paga'),
    ('Flutterwave', 'Flutterwave'),
    ('Interswitch', 'Interswitch'),
    ('Quickteller', 'Quickteller'),
    ('Paystack', 'Paystack'),
    ('Remita', 'Remita'),
    ('OPay', 'OPay'),
    ('Carbon (formerly Paylater)', 'Carbon (formerly Paylater)'),
    ('Kudi', 'Kudi'),
    ('PalmPay', 'PalmPay'),
]
        self.fields['recipient_bank_name'].choices = bank_choices

    def clean(self):
        cleaned_data = super().clean()
        recipient_account = cleaned_data.get("recipient_account")
        amount = cleaned_data.get("amount")

        # Validate recipient account number
        if not recipient_account:
            raise forms.ValidationError("Recipient account number is required.")

        # Validate amount
        if not amount:
            raise forms.ValidationError("Amount is required.")
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")

        return cleaned_data


class WithdrawForm(forms.Form):
    account_number = forms.CharField(label='Account Number')
    amount = forms.DecimalField(label='Amount')

class DepositForm(forms.Form):
    account_number = forms.CharField(label='Account Number')
    amount = forms.DecimalField(label='Amount')
