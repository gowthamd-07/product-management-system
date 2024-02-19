from django.urls import path

from . import views

urlpatterns = [
    path('uploadersignin', views.uploaderSignin, name='uploadersignin'), 
    path('viewersignin', views.viewerSignin, name='viewersignin'),
    path('verifiersignin', views.verifierSignin, name='verifiersignin'),
    path('logout', views.logout, name='logout')
]