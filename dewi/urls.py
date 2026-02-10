from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name='home'),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('error_404/', views.error_404, name='error_404'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('project/', views.project, name='project'),
    
    
]
