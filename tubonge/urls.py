from django.urls import path
from . import views

urlpatterns = [
    path('navbar', views.nav, name='nav'),
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
     path('footer',views.footer,name='footer'),
    
   
]