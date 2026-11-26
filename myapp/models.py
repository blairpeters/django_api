from django.db import models

CATEGORIES = [
    ("Personal Care", "Personal Care"),
    ("Sports", "Sports"),
    ("Clothing", "Clothing"),
    ("Food", "Food"),
]

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=20, unique=True)#every product code is unique
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.code}'
