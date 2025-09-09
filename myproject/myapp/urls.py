from django.urls import path
from . import views
app_name = 'myapp'

urlpatterns = [
    path('' ,views.index , name='index'),
    path('time_display' , views.index , name='index'),
    path('way2' ,views.way2 , name='way2')
]