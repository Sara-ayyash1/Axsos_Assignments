from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book' , views.add_book),
    path('book_detail/<int:id>' , views.book_detail),
    path('delete_book/<int:id>' , views.delete_book),
    path('edit_book/<int:id>', views.edit_book),
    path('authors', views.authors_index),
    path('add_author' , views.add_author),
    path('author_detail/<int:id>', views.author_detail),
]