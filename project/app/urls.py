from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_products, name='fetch_products'),
    path('simple/id', views.simple, name='simple')
]