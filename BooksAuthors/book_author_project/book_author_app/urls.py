from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('create_book' ,views.create_book ,name='create_book'),
    path('book/<int:id>' ,views.book_details ,name='book_details'),
    path('add_author_to_book/<int:id>' ,views.add_author_to_book ,name='add_author_to_book'),
    path('author' , views.author , name='author'),
    path('create_author', views.create_author ,name='create_author'),
    path('author/<int:id>' ,views.author_details ,name='author_details'),
    path('add_book_to_author/<int:id>' ,views.add_book_to_author ,name='add_book_to_author')

]