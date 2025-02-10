# # your_app_name/urls.py
# from django.urls import path
# from . import views

# app_name = 'products'  # This sets the namespace for your app

# urlpatterns = [
#     path('products/', views.fetch_products, name='products'),
#     path('product/<int:id>/', views.fetch_product_detail, name='product_detail'),
#     path('api/product/<int:id>/', views.get_product_api, name='product_api'),
# ]

from django.urls import path
from django.views.generic import RedirectView
from . import views  # Replace 'yourapp' with your app name

urlpatterns = [
    path('', RedirectView.as_view(url='/products/')),  # Redirect root to products
    path('products/', views.products, name='products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('api/product/<int:id>/', views.product_api, name='product_api'),
]