# blog/views.py
import requests
from django.shortcuts import render

def country_list(request):
    response = requests.get('https://restcountries.com/v3.1/all')
    countries = response.json()
    
    # Preprocess the capital field for each country
    for country in countries:
        capital = country.get('capital', [])
        if capital:
            country['capital'] = capital[0]  # Get the first capital if there are multiple
    
    return render(request, 'blog/country_list.html', {'countries': countries})


def country_detail(request, name):
    response = requests.get(f'https://restcountries.com/v3.1/name/{name}')
    country = response.json()[0]  # Get the first country in the response
    capital = country.get('capital', [])
    if capital:
        country['capital'] = capital[0]  # If capital exists, take the first one
    return render(request, 'blog/country_detail.html', {'country': country})