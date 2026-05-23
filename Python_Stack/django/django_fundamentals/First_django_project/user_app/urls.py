from django.urls import path
from . import views 
from first_app import views as blog_views 

urlpatterns = [
    path('users/new' , views.register),
    path('users' , views.index),
    path('register' , views.register),
    path('login', views.login),
    path('', blog_views.index), 
]
