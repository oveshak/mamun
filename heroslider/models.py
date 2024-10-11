from django.db import models

from allImages.models import SliderItem
from solo.models import SingletonModel

# Create your models here.
class HeroSlider(SingletonModel):
    name = models.CharField(max_length=20)
    slider_item = models.ManyToManyField(SliderItem)