from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

def fetch_products(request):
    api_url = "https://dummyjson.com/products"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'products.html', {'products': data['products']})
        else:
            return render(request, 'products.html', {'error': 'Failed to fetch data from the API'})
    except requests.exceptions.RequestException as e:
        return render(request, 'products.html', {'error': f'An error occurred: {str(e)}'})

def fetch_product_detail(request, id):
    api_url = f"https://dummyjson.com/products/{id}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            product = response.json()
            context = {
                'product': {
                    'name': product.get('title'),
                    'price': product.get('price'),
                    'description': product.get('description'),
                    'images': {
                        'main': product.get('thumbnail'),
                        'angles': product.get('images', [])
                    },
                    'specifications': [
                        {'name': 'Brand', 'value': product.get('brand')},
                        {'name': 'Category', 'value': product.get('category')},
                        {'name': 'Rating', 'value': product.get('rating')},
                        {'name': 'Stock', 'value': product.get('stock')},
                    ]
                }
            }
            return render(request, 'simple.html', context)
        else:
            return render(request, 'simple.html', {'error': f'Failed to fetch product with ID {id}'})
    except requests.exceptions.RequestException as e:
        return render(request, 'simple.html', {'error': f'An error occurred: {str(e)}'})

@api_view(['GET'])
def get_product_api(request, id):
    api_url = f"https://dummyjson.com/products/{id}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return Response(response.json())
        return Response({'error': 'Product not found'}, status=404)
    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=500)