from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.index, name='uploaderdashboard'),
    path('products', views.products, name='uploaderproducts'),
    path('addproduct', views.addProduct, name='uploaderaddproduct'),
    path('details/<int:id>', views.details, name='uploaderdetails'),
    path('edit/<int:id>', views.edit, name='uploaderedit'),
    path('delete/<int:id>', views.delete, name='uploaderdelete'),
    path('<int:id>', views.imageView, name='uploaderimageView')
    #path('update/<int:id>',views.update, name='uploaderupdate')
]