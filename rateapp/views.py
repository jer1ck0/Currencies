from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RequestForm, CurrencyForm
from .models import Rate
import datetime
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def index(request):
    if request.method == "POST":  
        first_currency = request.POST.get("first_currency")
        second_currency = request.POST.get("second_currency")
        period = (datetime.datetime.strptime(request.POST.get("period") + ' UTC', '%d-%m-%Y %H:%M %Z').astimezone() if request.POST.get("period") != "" else datetime.datetime.now().astimezone())
        logging.warning(period)
        result = Rate.comparing((first_currency, second_currency, period))
        requestform = RequestForm
        # return HttpResponse("Request = {0}, {1}, {2}, {3}".format(first_currency, second_currency, period, result))
        return render(request, "index.html", {"form": requestform, "result": result, "first_currency": first_currency, "second_currency": second_currency, "period": period})
    else:
        requestform = RequestForm
        return render(request, "index.html", {"form": requestform})


def new_currency(request):
    currencyform = CurrencyForm
    return render(request, "newcurrency.html", {"form": currencyform})

def currencies(request):
    rates = Rate.objects.all()
    return HttpResponse("Hello. There is list of currencies")

def create(request):
    if request.method == "POST":  
        currency = Rate()
        currency.ident = request.POST.get("currency_ident")
        currency.rate = request.POST.get("currency_rate")
        currency.time_point = datetime.datetime.strptime(request.POST.get("period"), '%d-%m-%Y %H:%M')
        currency.save()
        return HttpResponseRedirect("/")
    else:
        requestform = RequestForm
        return render(request, "index.html", {"form": requestform})

# Create your views here
