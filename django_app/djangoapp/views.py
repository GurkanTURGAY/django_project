from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course,Category

data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web geliştirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar"
}

db = {
    "courses" : [
        {
            "title" : "javascript kursu",
            "description" : "javascript kurs açıklaması",
            "imageUrl" : "1.jpg",
            "slug" : "javascript-kursu",
            "date" : datetime.now(),
            "isActive" : True
        },
        {
            "title" : "python kursu",
            "description" : "python kurs açıklaması",
            "imageUrl" : "2.jpg",
            "slug" : "python-kursu",
            "date" : datetime.now(),
            "isActive" : True
        },
        {
            "title" : "web geliştirme kursu",
            "description" : "web geliştirme kurs açıklaması",
            "imageUrl" : "3.jpg",
            "slug" : "web-gelistirme-kursu",
            "date" : datetime.now(),
            "isActive" : True
        }
    ],
    "categories" : [
        { "id": 1, "name": "programlama", "slug": "programlama"},
        { "id": 2, "name": "web geliştirme", "slug": "web-gelistirme"},
        { "id": 3, "name": "mobil uygulamalar", "slug": "mobil"},
    ]
}

# http://127.0.0.1:8000/kurslar

def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    # for kurs in db["courses"]:
    #     if kurs["isActive"] == True:
    #         kurslar.append(kurs)

    return render(request, 'courses/index.html', {
        'categories' : kategoriler,
        'courses' : kurslar
    }
    )

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course' : course
    } 
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(category__slug=slug, isActive=True)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories' : kategoriler,
        'courses' : kurslar,
        'seciliKategori' : slug
    })