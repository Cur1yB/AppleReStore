from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.type.name} {self.name}"

class Product(models.Model):
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.product_model.name} - {self.price}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images')

    def __str__(self):
        return f"Image for {self.product.product_model.name}"

