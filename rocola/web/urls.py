from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getalbums/', views.getalbums, name='getalbums'),
    path('detalle/', views.detalle, name='detalle'),
]
