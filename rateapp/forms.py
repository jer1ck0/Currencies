from django import forms
 
class RequestForm(forms.Form):
    first_currency = forms.CharField()
    second_currency = forms.CharField()
    period = forms.DateTimeField(required=False)

class CurrencyForm(forms.Form):
    currency_ident = forms.CharField()
    currency_rate = forms.CharField()
    period = forms.DateTimeField()