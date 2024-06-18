from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('anasayfa sayfası')

def hakkimizda(request):
    return HttpResponse('hakkimizda sayfası')

def iletisim(request):
    return HttpResponse('iletisim sayfası')