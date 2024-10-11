from django.db import models
from django.utils.text import slugify
# Create your models here.
class SubCategory(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,default="", null=False,unique=True)
   
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            num = 1
            while SubCategory.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}/{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,default="", null=False,unique=True)
    subcategory=models.ManyToManyField(SubCategory , blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            num = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}/{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    



