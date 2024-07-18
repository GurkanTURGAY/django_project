from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="",null=False,unique=True,db_index=True, max_length=50)
    weight = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101,10)))

    def __str__(self):
        return f"{self.name}"



class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images",default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isHome = models.BooleanField(default=True)
    slug = models.SlugField(default="",blank=True, null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)


    def __str__(self):
        return f"{self.title}"
    
class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")