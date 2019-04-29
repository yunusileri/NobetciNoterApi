from django.http import JsonResponse
from django.shortcuts import render
import json
from verial.main import *


# Create your views here.

def sorgula(request):
    data = Istek(request.GET.get('Tarih'), request.GET.get('Sehir'))
    veri = Data(data)

    return JsonResponse(veri, safe=False)


dict = {'Türker': 10}
