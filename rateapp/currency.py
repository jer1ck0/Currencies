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
        query_set = Rate.objects.filter(ident=currency).order_by('time_point')
        start_index = 0
        end_index = len(query_set) - 1
        while True:
            index = int(((start_index + end_index)/2)//1)
            if query_set[index].time_point == date:
                return query_set[index].rate
            elif query_set[index].time_point < date:
                start_index = index + 1
            else:
                end_index = index - 1
            if start_index > end_index:
                return query_set[index].rate
    
    def compare(currency1, currency2, date):
        result = CurrencyRates.find(currency1, date)/CurrencyRates.find(currency2, date)
        result = {'status': 'Successfull', 
            'compare_result': result}
        return result

