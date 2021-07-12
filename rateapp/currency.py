import datetime
from .models import Rate

class CurrencyRates():
    def add(currency, rate, date):
        if len(Rate.objects.filter(ident=currency, time_point = date)) == 0:
            result = Rate(ident = currency, rate = rate, time_point = date)
            result.save()
            result = {'status': 'Successfull', 
                      'currency':{'ident': result.ident, 
                                  'rate': result.rate,
                                  'time_point': result.time_point
                                 }
                     }
            return result
        else:
            result = {'status': 'Bad request. Rate already in base'}
            return result

    def find(currency, date):
        return Rate.objects.filter(ident=currency, time_point__lte=date).order_by('-time_point')[0].rate

    
    def compare(currency1, currency2, date):
        result = CurrencyRates.find(currency1, date)/CurrencyRates.find(currency2, date)
        result = {'status': 'Successfull', 
            'compare_result': result}
        return result

