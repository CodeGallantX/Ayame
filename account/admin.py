from django.contrib import admin
from .models import CustomUser, AccountData

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AccountData)