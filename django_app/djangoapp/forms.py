from django import forms

from djangoapp.models import Course

"""
class CourseCreateForm(forms.Form):
    title = forms.CharField(label="Kurs Başlığı",
                            required=True,
                            error_messages={
                                "required":"Kurs Başlığı Girmelisiniz."
                            },
                            widget= forms.TextInput(attrs={"class":"form-control"})
                            )

    description = forms.CharField(label="Kurs Açıklaması",
                                  error_messages={
                                      "required":"Kurs Açıklaması Girmelisiniz."
                                  },
                                  widget=forms.Textarea(attrs={"class":"form-control"}))
    
    imageUrl = forms.CharField(error_messages={
                                "required":"image Url Alanı Girmelisiniz."
                            },
                            widget= forms.TextInput(attrs={"class":"form-control"}))
    
    slug = forms.SlugField(error_messages={
                                "required":"Slug Alanı Girmelisiniz."
                            },
                            widget= forms.TextInput(attrs={"class":"form-control"}))"""

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'categories','description', 'image')
        labels = {
            'title':"İha'yı Kiralayacak Kişinin Adı:",
            'description':"İhanın Menşei:",
            'categories':"Kiralanacak İha(Marka/Model):",
            'image':"Fotoğrafınızı yükleyin:"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required": "İha'yı Kiralayacak Kişinin İsmini Girmelisiniz."
            },
            "description":{
                "required": "İhanın Markasını Girmelisiniz."
            },
            "categories":{
                "required": "Kiralanacak İhayı Seçmelisiniz."
            }
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description', 'image','categories')
        labels = {
            'title':"İha'yı Kiralayacak Kişinin Adı:",
            'description':"İhanın Menşei:",
            'categories':"Kiralanacak İha(Marka/Model):",
            'image':"Fotoğrafınızı yükleyin:"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"}),
            "categories": forms.SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required": "İha'yı Kiralayacak Kişinin İsmini Girmelisiniz."
            },
            "description":{
                "required": "İhanın Markasını Girmelisiniz."
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField()