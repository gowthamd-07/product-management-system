from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.index, name='verifierdashboard'),
    path('products', views.products, name='verifierproducts'),
    path('details/<int:id>', views.details, name='verifierdetails'),
    path('edit/<int:id>', views.edit, name='verifieredit'),
    path('delete/<int:id>', views.delete, name='verifierdelete'),
    path('<int:id>', views.imageView, name='verifierimageView'),

]