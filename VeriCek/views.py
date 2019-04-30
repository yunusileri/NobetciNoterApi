import json

from django.http import JsonResponse

from VeriCek.data_selenium import *


def sorgula(request):
    tarih = request.GET.get('Tarih')
    sehir = request.GET.get('Sehir')

    data = data_get(tarih, sehir)

    veri = data_split(data)

    return JsonResponse(json.dumps(veri), safe=False)
