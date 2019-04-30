import json

from django.http import JsonResponse

from VeriCek.data_selenium import *


def sorgula(request):
    tarih = request.GET.get('Tarih')
    sehir = request.GET.get('Sehir')

    data = data_get(tarih, sehir)
    return JsonResponse(json.dumps(data), safe=False)
