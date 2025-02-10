from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

import requests
from django.shortcuts import render

def fetch_products(request):
    # API endpoint URL
    api_url = "https://dummyjson.com/products"
    
    try:
        # Send GET request to the API
        response = requests.get(api_url)
        
        # If the response status code is 200 (OK), return the data
        if response.status_code == 200:
            data = response.json()  # Parse JSON data from the API response
            return render(request, 'products.html', {'products': data['products']})
        else:
            return render(request, 'products.html', {'error': 'Failed to fetch data from the API'})
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network errors)
        return render(request, 'products.html', {'error': f'An error occurred: {str(e)}'})
    
def simple(request,id):

    return render(request,'simple.html')