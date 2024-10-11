from django.db import models
from django.utils.text import slugify
from category.models import Category, SubCategory
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, default="", null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug
            self.slug = slugify(self.product_name)
            unique_slug = self.slug
            num = 1
            # Ensure the slug is unique
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(Product, self).save(*args, **kwargs)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_quantity = models.IntegerField(default=0)  # Fixed typo here
    product_image = models.ImageField(upload_to='products/')
    product_rating = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(5)]  # Ensure rating is between 0 and 5
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
