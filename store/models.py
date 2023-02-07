from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ("Shirts", "Shirts"),
    ("Jeans", "Jeans"),
    ("Sweatshirt", "Sweatshirt"),
    ("Hoody", "Hoody"),
    ("Gown", "Gown")

)

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    image = models.ImageField(upload_to="product_images")
    price = models.FloatField()
    discount_price = models.TextField()


    
    def __str__(self):
        return self.name
