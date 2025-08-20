from django.shortcuts import render
from googletrans import Translator, LANGUAGES
from forex_python.converter import CurrencyRates, CurrencyCodes
from django.http import JsonResponse

def home(request):
    return render(request, 'converter/home.html')

# Create your views here.
def translate_text(request):
    return render(request,'translate.html')

def convert_currency(request):
    return render(request,'convert_currency.html')


