from django.urls import path
from . import views # the dot means the views file is in the same directory as this file

# urlpatterns = [
#         path('bears', views.one_method),                        # would only match localhost:8000/bears
#         path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
#         path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
#         path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
# ]

urlpatterns = [
    path('', views.root),
    path('blogs' , views.index),
    path('blogs/new' , views.new),
    path('blogs/create' , views.create),
    path('blogs/<int:number>' , views.show),
    path('blogs/<int:number>/edit' , views.edit),
    path('blogs/<int:number>/delete' , views.destroy),
    path('blogs/blog_json' , views.json),
]
