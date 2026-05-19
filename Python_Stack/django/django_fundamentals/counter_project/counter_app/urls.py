from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index ),
    path('destroy_session' , views.destroy_session),
    path('increment_count_2' , views.increment_count_2),
    path('increment_by' , views.increment_by)
]