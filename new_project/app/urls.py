from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('arma', views.arma),
    path('dji', views.dji),
    path('photos', views.photos),
    path('contact', views.contact)
]