from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RequestForm, CurrencyForm
from .models import Rate
from .currency import *
import datetime
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def add(request):
    currency = request.GET['cur']
    rate = request.GET['rate']
    try:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%dT%H:%M:%S")
    except:
        date = datetime.datetime.now()
    result = Rate.add(currency, rate, date)
    return HttpResponse("Request = {}".format(result))

def compare(request):
    print(request.GET)
    currency1 = request.GET['1c']
    currency2 = request.GET['2c']
    try:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%dT%H:%M:%S")
    except:
        date = datetime.datetime.now()
    result = Rate.compare(currency1, currency2, date)
    return HttpResponse("Request = {}".format(result))

def all_rates(request = None):
    return HttpResponse("Request = {}".format(Rate.rates))

# Create your views here
