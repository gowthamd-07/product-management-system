from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.index, name='viewerdashboard'),
    path('products', views.products, name='viewerproducts'),
    path('magentoproducts', views.magentoproducts, name='viewermagentoproducts'),
    path('details/<int:id>', views.details, name='viewerdetails'),
    path('edit/<int:id>', views.edit, name='vieweredit'),
    path('delete/<int:id>', views.delete, name='viewerdelete'),
    path('remove/<int:id>', views.remove, name='viewerremove'),
    path('<int:id>', views.imageView, name='viewerimageView')

]