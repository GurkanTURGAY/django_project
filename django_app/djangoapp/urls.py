from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('iha-kirala', views.create_course, name="iha_kirala"),
    path('iha-listesi',views.course_list, name="iha_listesi"),
    path('kira-güncelle/<int:id>',views.course_edit,name="course_edit"),
    path('kira-sil/<int:id>',views.course_delete,name="course_delete"),
    path('upload',views.upload,name="upload_image"),
    path('<slug:slug>', views.details, name="course_details"),
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]
