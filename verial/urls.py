from django.urls import path
from verial.views import *

app_name = 'verial'

urlpatterns = [
    path('sorgula', sorgula)
]
