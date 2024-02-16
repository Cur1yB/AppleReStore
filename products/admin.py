from django.contrib import admin
from .models import Product, ProductType, ProductModel, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Количество форм для добавления новых изображений по умолчанию

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_model', 'price', 'description') 
    list_filter = ('product_model__type', 'product_model__name')
    search_fields = ('description', 'product_model__name')
    inlines = [ProductImageInline] 

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
