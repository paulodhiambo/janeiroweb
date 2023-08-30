from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms

from hospital.models import Article


class ArticleAdminForm(forms.ModelForm):
    content = RichTextUploadingFormField()

    class Meta:
        model = Article
        fields = '__all__'
