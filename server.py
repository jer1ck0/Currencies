from datetime import date
from currency import Rate, rates
from flask import Flask, json, request

app = Flask(__name__)

@app.route("/base")
def base_info():
    return rates


@app.route("/compare")
def comparing():
    currency1 = request.args.get('1c')
    currency2 = request.args.get('2c')
    day, month, year = request.args.get('date').split('-') if request.args.get('date') != None else [date.today().day, date.today().month, date.today().year]
    target_request = (currency1, currency2, int(year), int(month), int(day))
    if currency1 == None or currency2 == None:
        return "Wrong format of request"
    else:
        target = Rate.compare(target_request)
        return str(target)
      
@app.route("/add")
def adding():
    currency = request.args.get('cur')
    rate = request.args.get('rate')
    day, month, year = request.args.get('date').split('-') if request.args.get('date') != None else [date.today().day, date.today().month, date.today().year]
    target_request = (currency, rate, int(year), int(month), int(day))
    if currency == None or rate == None:
        return "Wrong format of adding request"
    else:
        Rate.add(target_request)
        return f"Added rate{rates}"

if __name__ == '__main__':
    app.run(host='45.143.136.88', port='5000', debug=True)