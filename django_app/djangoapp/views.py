from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# http://127.0.0.1:8000/        > anasayfa
# http://127.0.0.1:8000/home    > anasayfa
# http://127.0.0.1:8000/kurslar > kurslar

def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('kurs listesi')