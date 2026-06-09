from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('courses/add_course/' , views.add_course),
    path('courses/destroy/<int:course_id>/' , views.destroy_course , name='destroy_course'),
    path('courses/add_comment/<int:course_id>/' , views.new_comment , name='new_comment'),
    path('courses/create_comment/<int:course_id>/', views.create_comment, name='create_comment'),
]
