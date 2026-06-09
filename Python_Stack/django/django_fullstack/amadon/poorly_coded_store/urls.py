from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy/', views.buy, name='buy'),
    path('checkout/', views.checkout),
    path('clear/', views.clear_session, name='clear_session'),
]
