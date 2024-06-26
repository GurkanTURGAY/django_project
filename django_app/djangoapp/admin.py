from django.contrib import admin
from .models import Course,Category

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category")
    list_display_links = ("title","slug")
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("isActive","category")
    list_editable = ("isActive",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    prepopulated_fields = {"slug": ("name",),}