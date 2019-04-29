from django.urls import path
from VeriCek.views import *

app_name = 'VeriCek'

urlpatterns = [
    path('sorgula', sorgula)
]
