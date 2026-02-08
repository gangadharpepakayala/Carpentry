from django.contrib import admin
from . models import User,Order,Sell

# Register your models here.
admin.site.register(User)

admin.site.register(Order)

admin.site.register(Sell)