global base
base = ()


def add_currency(name, period):
    rate = input('input rate')
    period = time.strftime('%H%M')
    period = time.time()
    return (name, rate, period)

def findRate(currency, period):
    currency_rates = [element for element in base if currency in element]
    target_rates = [element for element in currency_rates if period - int(element[2]) >= 0]
    rate = min(target_rates, key=lambda i : period - int(i[2]))[1]
    return int(rate)

if __name__ == '__main__':
    question = input('Do you want add start rate list? ')
    if question == 'yes':
        while True:
            currency = input('Pls input currency. If you finish adding currencies input STOP ')
            if currency != 'STOP': 
                rate = input('Pls input rate ')        
                time = input('time in format HHMM ') 
                base += ((currency, rate, time),)
                print (base)
            else:
                break
    while True:
        request = input('pls input your request in format <first_currency>, <second_currency>, <compare_period>')
        first_currency = input('input first currency ')
        if first_currency not in [element[0] for element in base]:
            currency = add_currency(first_currency)
            base += (currency,)
            print(base)
        else:
            request.append(first_currency)
        second_currency = input('input second currency ')
        if second_currency not in [element[0] for element in base]:
            currency = add_currency(second_currency)
            base += (currency,)
        else:
            request.append(second_currency)    
        period = input('input period in format HHMM ')
        if period == '':
            request.append(0)
        else:
            request.append(period) 
        target = findRate(request[0], int(request[2]))/findRate(request[1], int(request[2]))
        print (target)
        # rates_a = [element for element in base if request[0] in element]
        # rates_target = [el for el in rates_a if int(request[2])- int(el[2]) >= 0]
        # rate_a = min(rates_target, key=lambda i : int(request[2]) - int(i[2]))[1]
        request = []
        print(base)