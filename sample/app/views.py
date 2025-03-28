from django.shortcuts import render
from .models import *
from . serializers import *
from django.http import JsonResponse


def fun2(requset):
    if requset.method == 'GET':
        d=students.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)