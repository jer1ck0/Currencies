import datetime
global rates
rates = {"USD": [(datetime.date(2021, 5, 1), 71), (datetime.date(2021, 5, 2), 72), (datetime.date(2021, 5, 3), 73), (datetime.date(2021, 5, 4), 74), (datetime.date(2021, 5, 5), 75)],
         "RUB": [(datetime.date(2021, 5, 1), 1), (datetime.date(2021, 5, 2), 2), (datetime.date(2021, 5, 3), 3), (datetime.date(2021, 5, 4), 4), (datetime.date(2021, 5, 5), 5)]}

class Rate():

    def add(request):
        currency = request[0]
        rate = request[1]
        date = datetime.date(request[2], request[3], request[4])
        print (currency, rate, date)
        print (rates[currency])
        print (date not in [element[0] for element in rates[currency]])
        if date not in [element[0] for element in rates[currency]]:
            rates[currency].append((date, rate))
            rates[currency].sort()
            return "Succesfull added rate"
        else:
            return "Rate already exist"

    def find(currency, date = datetime.date.today()):
        start_index = 0
        end_index = len(rates[currency]) - 1
        while True:
            index = int(((start_index + end_index)/2)//1)
            if rates[currency][index][0] == date:
                return rates[currency][index][1]
            elif rates[currency][index][0] < date:
                start_index = index + 1
            else:
                end_index = index - 1
            if start_index > end_index:
                return rates[currency][index][1]
    
    def compare(request):
        date = datetime.date(request[2], request[3], request[4])
        return Rate.find(request[0], date)/Rate.find(request[1], date)

            