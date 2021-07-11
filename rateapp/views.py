from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from .forms import RequestForm, CurrencyForm
from .models import Rate
from .currency import *
import datetime
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def add(request):
    # try:
    currency = request.GET['cur']
    rate = request.GET['rate']
    try:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    except:
        date = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
    result = CurrencyRates.add(currency, rate, date)
    return JsonResponse(result, safe=False)
    # except:
        # return HttpResponse("Bad format of request. Pls send next args: 'c1', 'c2', 'date' in ISO format")

def compare(request):
    currency1 = request.GET['1c']
    currency2 = request.GET['2c']
    try:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    except:
        date = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
    result = CurrencyRates.compare(currency1, currency2, date)
    return JsonResponse(result, safe=False)

def all_rates(request = None):
    serializers.serialize("json", Rate.objects.all())
    result = serializers.serialize("json", Rate.objects.all())
    return JsonResponse(result, safe=False)

# Create your views here
