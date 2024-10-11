from django.db import models

# Create your models here.
class SliderItem(models.Model):
    title= models.CharField(max_length=20)
    image=models.ImageField(upload_to="slider/")
  
    def __str__(self):
        return self.title
    

