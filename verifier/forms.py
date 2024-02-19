from django.apps import apps
from django import forms
#from proactivehome.models import Product

Product = apps.get_model('proactivehome', 'Product')

class Productforms(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['magento_id']