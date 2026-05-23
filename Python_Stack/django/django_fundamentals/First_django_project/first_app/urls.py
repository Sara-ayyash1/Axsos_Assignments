from django.urls import path
from . import views # the dot means the views file is in the same directory as this file

# urlpatterns = [
#         path('bears', views.one_method),                        # would only match localhost:8000/bears
#         path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
#         path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
#         path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
# ]

urlpatterns = [
    path('', views.index),
    path('new' , views.new),
    path('create' , views.create),
    path('<int:number>' , views.show),
    path('<int:number>/edit' , views.edit),
    path('<int:number>/delete' , views.destroy),
    path('json' , views.blog_json),
]
