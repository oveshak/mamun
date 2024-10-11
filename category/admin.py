from django.contrib import admin

from category.models import Category, SubCategory

# Register your models here.
admin.site.register(SubCategory)
admin.site.register(Category)