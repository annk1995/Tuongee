from django.urls import path
from . import views

urlpatterns = [
    path('navbar', views.nav, name='nav'),
    path('index', views.index, name='index'),
    path('about',views.about,name='about'),
     path('footer',views.footer,name='footer'),
     path('contact',views.contact,name='contact')
    
   
]