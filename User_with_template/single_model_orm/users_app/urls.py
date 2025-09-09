from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_user', views.create_user, name='create_user'),

]
