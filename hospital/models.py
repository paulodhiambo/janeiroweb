from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django_slugify_processor.text import slugify


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextUploadingField()
    cover_image = models.ImageField()
    created_at = models.DateTimeField(auto_created=True)
    published_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def title_summary(self) -> str:
        if len(self.title) > 60:
            return self.title[:60]
        else:
            return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])
