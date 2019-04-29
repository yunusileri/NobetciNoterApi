from django.http import JsonResponse
from VeriCek.data_selenium import *


def sorgula(request):
    data = data_get(request.GET.get('Tarih'), request.GET.get('Sehir'))
    veri = data_split(data)

    return JsonResponse(veri, safe=False)
