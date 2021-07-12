from django import forms
 
class RequestForm(forms.Form):
    first_currency = forms.CharField(max_length=3, min_length=3)
    second_currency = forms.CharField(max_length=3, min_length=3)
    period = forms.DateTimeField()

class CurrencyForm(forms.Form):
    ident = forms.CharField(max_length=3, min_length=3)
    rate = forms.FloatField(min_value=0.0)
    period = forms.DateTimeField()