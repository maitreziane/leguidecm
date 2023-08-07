from django.contrib import admin
from apps.product.models import Product, Images, Category_product
# Register your models here.Category_product


class ProductAdmin(admin.ModelAdmin):
    
    list_display= ["title", "category", "ville", "price"]
    
class ImageAdmin(admin.ModelAdmin):
    
    list_display =["model", "image"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Category_product)
