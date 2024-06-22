from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('kurslar/', include('djangoapp.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
