from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms

from hospital.models import Article, Career


class ArticleAdminForm(forms.ModelForm):
    content = RichTextUploadingFormField()

    class Meta:
        model = Article
        fields = '__all__'


class CareerAdminForm(forms.ModelForm):
    content = RichTextUploadingFormField()

    class Meta:
        model = Career
        fields = '__all__'
