from django.urls import path

from . import views

urlpatterns =[
    path('', views.register, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.Userlogin, name='login'),

    path('about/', views.about, name='about'),
    path('service-details/', views.servicepage ,name='service-details'),
    path('starter-page/', views.starterpage ,name='starter'),

]