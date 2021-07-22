from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from .forms import RequestForm, CurrencyForm
from .models import Rate, User
from .currency import *
import datetime
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def add(request):
    try: 
        current_user = User.objects.get(key=request.headers["Api-Key"])
        if current_user.role == 2:
            data = {}
            data['ident'] = request.GET['cur']
            data['rate'] = request.GET['rate']
            try:
                data['period'] = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=datetime.timezone.utc)
            except:
                data['period'] = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
            f = CurrencyForm(data)
            print (data)
            if f.is_valid():
                result = CurrencyRates.add(data['ident'], data['rate'], data['period'])
                return JsonResponse(result, safe=False)
            else:
                return JsonResponse(f.errors.as_json(), safe=False)
        else:
            return JsonResponse({"status_code": 401, "detail": "Not authorized"}, safe=False)
    except:
        return JsonResponse({"status_code": 401, "detail": "User not found"}, safe=False)

def compare(request):
    try: 
        current_user = User.objects.get(key=request.headers["Api-Key"])
        if current_user.role in (1,2):
            data = {}
            data['first_currency'] = request.GET['1c']
            data['second_currency'] = request.GET['2c']
            try:
                data['period'] = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=datetime.timezone.utc)
            except:
                data['period'] = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
            f = RequestForm(data)
            if f.is_valid():
                result = CurrencyRates.compare(data['first_currency'], data['second_currency'], data['period'])
                return JsonResponse(result, safe=False)
            else:
                return JsonResponse(f.errors.as_json(), safe=False)
        else:
            return JsonResponse({"status_code": 401, "detail": "Not authorized"}, safe=False)
    except:
        return JsonResponse({"status_code": 401, "detail": "User not found"}, safe=False)

def all_rates(request):
    try: 
        current_user = User.objects.get(key=request.headers["Api-Key"])
        if current_user.role in (1,2):
            result = serializers.serialize("json", Rate.objects.all())
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse({"status_code": 401, "detail": "Not authorized"}, safe=False)
    except:
        return JsonResponse({"status_code": 401, "detail": "User not found"}, safe=False)

# Create your views here
