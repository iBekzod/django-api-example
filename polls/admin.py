from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Category, Product, Customer, Order, Detail, Invoice, Payment)
class AppAdmin(admin.ModelAdmin):
    pass