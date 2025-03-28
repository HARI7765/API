from django.urls import path
from .  import views

urlpatterns = [
    path('', views.fun2, name='fun2'),
  
]
