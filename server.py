import datetime
from currency import Rate
from flask import Flask, json, request

app = Flask(__name__)

@app.route("/base")
def base_info():
    return Rate.rates


@app.route("/compare")
def comparing():
    currency1 = request.args.get('1c')
    currency2 = request.args.get('2c')
    date = datetime.datetime.now() if request.args.get('date') == None else datetime.datetime.strptime(request.args.get('date'), "%Y-%m-%dT%H:%M:%S")
    if currency1 == None or currency2 == None:
        return "Wrong format of request"
    else:
        target = Rate.compare(currency1, currency2, date)
        return str(target)
      
@app.route("/add")
def adding():
    currency = request.args.get('cur')
    rate = request.args.get('rate')
    date = datetime.datetime.now() if request.args.get('date') == None else datetime.datetime.strptime(request.args.get('date'), "%Y-%m-%dT%H:%M:%S")
    if currency == None or rate == None:
        return "Wrong format of adding request"
    else:
        Rate.add(currency, rate, date)
        return Rate.rates

if __name__ == '__main__':
    app.run(host='45.143.136.88', port='5000', debug=True)