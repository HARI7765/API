from django.shortcuts import render
from .models import *
from . serializers import *
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


def fun2(requset):
    if requset.method == 'GET':
        d=students.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)

def fun3 (request):
    if request.method == 'GET':
        d=students.objects.all()
        s=model_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    
    elif request.method == 'POST':
        d=JSONParser().parse(request)
        s=model_serializer(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
        
def fun4 (request,d):
    try:
        demo =demo.objects.get(pk=d)
    except students.DoesNotExist:
        return HttpResponse('inavalid')
    if request.method == 'GET':
        s=model_serializer(demo)
        return JsonResponse(s.data)
    elif request.method == 'PUT':
        d=JSONParser().parse(request)
        s=model_serializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif request.method == 'DELETE':
            demo.delete()
            return HttpResponse('deleted')