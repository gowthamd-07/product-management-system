from django.contrib import admin
from .models import Product, Product_modified, ProductInMagento, ProductImages

# Register your models here.
class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]

    class Meta:
        model = Product

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass




#admin.site.register(Product)
admin.site.register(Product_modified)
admin.site.register(ProductInMagento)