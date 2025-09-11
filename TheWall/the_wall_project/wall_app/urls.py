from django.urls import path ,include
from . import views

urlpatterns = [
    path('' ,views.index  , name='index'),
    path('register' , views.register , name='register'),
    path('login' , views.login , name='login'),
    path('logout' , views.logout ,name='logout'),
    path('home_page' , views.home_page , name='home_page'),

    path('post_message' ,views.post_message , name='post_message'),
    path('add_comment/<int:post_id>' ,views.add_comment , name='add_comment' )
]