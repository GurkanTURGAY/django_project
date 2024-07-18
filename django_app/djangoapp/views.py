from django.shortcuts import get_object_or_404, redirect, render
from djangoapp.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Course,Category, UploadModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test


# http://127.0.0.1:8000/kurslar

def index(request):
    kurslar = Course.objects.filter(isActive=1, isHome=1).order_by("title")
    kategoriler = Category.objects.all()

    # for kurs in db["courses"]:
    #     if kurs["isActive"] == True:
    #         kurslar.append(kurs)

    return render(request, 'courses/index.html', {
        'categories' : kategoriler,
        'courses' : kurslar
    }
    )

def isAdmin(user):
    return user.is_superuser

@login_required()
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/ihalar")
    else:
        form = CourseCreateForm()
    return render(request, "courses/iha-kirala.html", {"form":form})

@login_required()
def course_list(request):
    kiralayan = Course.objects.all()
    ihalar = Category.objects.all()

    return render(request, 'courses/iha-listesi.html', {
        'courses' : kiralayan,
        'category' : ihalar,
    }
    )

@login_required()
def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        form.save()
        return redirect("iha_listesi")
    else:
        form = CourseEditForm(instance=course)

    return render(request, 'courses/iha-kira-edit.html', {"form":form})

@login_required()
def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method =="POST":
        course.delete()
        return redirect("iha_listesi")

    return render(request, "courses/iha-delete.html", {"course":course})

@login_required()
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_image = request.FILES["image"]
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request,'courses/success.html')
    else:
        form = UploadForm()
    return render(request,'courses/upload.html',{"form":form})
    
@login_required()
def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by("title")
        kategoriler = Category.objects.all()
    else:
        return redirect("iha_listesi")

    return render(request, 'courses/search.html', {
        'categories' : kategoriler,
        'courses' : kurslar,
    })


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course' : course
    } 
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("title")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories' : kategoriler,
        'page_obj' : page_obj,
        'seciliKategori' : slug
    })