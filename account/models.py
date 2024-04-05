from django.db import models

class AccountData(models.Model):
    user = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    account_number = models.IntegerField(unique=True)