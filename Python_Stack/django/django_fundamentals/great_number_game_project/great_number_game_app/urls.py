from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('reset', views.reset),
    path('submit_winner', views.submit_winner),
    path('leaderboard', views.leaderboard),
]