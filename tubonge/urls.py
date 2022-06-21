from django.urls import path
from . import views

urlpatterns = [
    path('navbar', views.nav, name='nav'),
    path('', views.index, name='index'),
   
]