from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def expired_invoices(request):
    # return HttpResponse(Invoice.objects.is_expired())
    return Invoice.objects.filter(
        due > timezone.now()
    )

def wrong_date_invoices(request):
    return HttpResponse()

