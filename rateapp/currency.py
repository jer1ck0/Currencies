import datetime

class Rate():
    rates = {"USD": [(datetime.datetime(2021, 5, 1), 71), (datetime.datetime(2021, 5, 2), 72), (datetime.datetime(2021, 5, 3), 73), (datetime.datetime(2021, 5, 4), 74), (datetime.datetime(2021, 5, 5), 75)],
         "RUB": [(datetime.datetime(2021, 5, 1), 1), (datetime.datetime(2021, 5, 2), 2), (datetime.datetime(2021, 5, 3), 3), (datetime.datetime(2021, 5, 4), 4), (datetime.datetime(2021, 5, 5), 5)]}

    def add(currency, rate, date):
        print(type(date))
        if date not in [element[0] for element in Rate.rates[currency]]:
            Rate.rates[currency].append((date, int(rate)))
            Rate.rates[currency].sort()
            return "Succesfull added rate"
        else:
            return "Rate already exist"

    def find(currency, date):
        start_index = 0
        end_index = len(Rate.rates[currency]) - 1
        while True:
            index = int(((start_index + end_index)/2)//1)
            if Rate.rates[currency][index][0] == date:
                return Rate.rates[currency][index][1]
            elif Rate.rates[currency][index][0] < date:
                start_index = index + 1
            else:
                end_index = index - 1
            if start_index > end_index:
                return Rate.rates[currency][index][1]
    
    def compare(currency1, currency2, date):
        return Rate.find(currency1, date)/Rate.find(currency2, date)

