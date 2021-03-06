from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='images_created')
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300,blank=True)
    url = models.URLField()
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateField(auto_now=True,db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="images_liked",blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            print(self.title)
            print(slugify(self.title))
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)