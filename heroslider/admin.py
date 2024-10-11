from django.contrib import admin

from solo.admin import SingletonModelAdmin
from heroslider.models import HeroSlider

# Register your models here.
admin.site.register(HeroSlider,SingletonModelAdmin)