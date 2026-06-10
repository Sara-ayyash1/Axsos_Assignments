from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.index),
    path('add_message/' , views.create_message),
    path('add_comment/' , views.create_comment),
    path('delete_message/<int:message_id>/', views.delete_message)
]
