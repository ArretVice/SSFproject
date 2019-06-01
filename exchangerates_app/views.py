from django.shortcuts import render
import requests
import json


# Create your views here.
def rates_view(request):
    bases = ['USD', 'EUR']
    url_currencies = 'https://api.ratesapi.io/api/latest'
    data = {}
    current_date = None
    for base in bases:
        req = requests.get(url_currencies, params = {'base': base, 'symbols': ['RUB']})
        req = json.loads(req.text)
        if current_date == None:
            current_date = req['date']
        data[base] = req['rates']['RUB']
    return render(request, 'exchangerates_app/rates.html', {'data': data, 'current_date': current_date})
