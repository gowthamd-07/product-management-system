from django.db import models
from datetime import date

class Product(models.Model):
    product_id = models.CharField(max_length=30, blank=True)
    location_id = models.CharField(max_length=30, blank=True)
    building = models.IntegerField(default = 0)
    floor = models.IntegerField(default = 0)
    unit = models.CharField(max_length=20, blank=True)
    row = models.CharField(max_length=10, blank=True)
    column = models.CharField(max_length=10, blank=True)
    pallet = models.IntegerField(default = 0)
    level = models.CharField(max_length=10, blank=True)
    dimension = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=300, blank=True)
    quantity = models.IntegerField(default = 0)
    make_brand = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50, blank=True)
    price = models.FloatField(default = 0)
    product_link = models.URLField(max_length=500, blank=True)
    #product_image = models.ImageField(default=None, blank=True)

    def __str__(self):
        return str(self.pk) + " " + self.location_id

    def imagefoldername(self):
        return str(self.pk)

class Product_modified(models.Model):
    uploaded_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    uploaded_product = models.BooleanField(default=True)
    verified_product = models.BooleanField(default=False)
    uploaded_product_magento = models.BooleanField(default= False)
    product_pk = models.ForeignKey(Product, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.pk)
    
class ProductInMagento(models.Model):
    mproduct_id = models.CharField(max_length=30, blank=True)
    mmagento_id = models.CharField(max_length=30, default=None, blank=True)
    mlocation_id = models.CharField(max_length=30, default=None, blank=True)
    mbuilding = models.IntegerField(default=None, blank=True)
    mfloor = models.IntegerField(default=None, blank=True)
    munit = models.CharField(max_length=20, default=None, blank=True)
    mrow = models.CharField(max_length=10, default=None, blank=True)
    mcolumn = models.CharField(max_length=10, default=None, blank=True)
    mpallet = models.IntegerField(default=None, blank=True)
    mlevel = models.CharField(max_length=10, default=None, blank=True)
    mdimension = models.CharField(max_length=20, default=None, blank=True)
    mweight = models.CharField(max_length=20, default=None, blank=True)
    mdescription = models.TextField(max_length=300, default=None, blank=True)
    mquantity = models.IntegerField(default=None, blank=True)
    mmake_brand = models.CharField(max_length=50, default=None, blank=True)
    msource = models.CharField(max_length=50, default=None, blank=True)
    mprice = models.FloatField(default=None, blank=True)
    mproduct_link = models.URLField(max_length=500, default=None, blank=True)

    def __str__(self):
        return str(self.pk) + " " + self.mlocation_id

class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productImages')

    # def __str__(self):
    #     return self.product.product_id

class ProductInMagentoImages(models.Model):
    mproduct = models.ForeignKey(ProductInMagento, default=None, blank=True, on_delete=models.CASCADE)
    mimage = models.ImageField(upload_to = 'mproductImages')