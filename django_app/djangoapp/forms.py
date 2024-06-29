from django import forms

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
                            widget= forms.TextInput(attrs={"class":"form-control"}))