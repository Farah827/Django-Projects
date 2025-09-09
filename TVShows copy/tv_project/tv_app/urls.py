from django.urls import path ,include
from . import views

urlpatterns =[
    path('' , views.index ,name='index' ),
    path('create_show' ,views.create_show,name='create_show'),
    path('<int:id>',views.show_details , name='show_details'),
    path('edit/<int:id>' , views.edit_show, name='edit_show'),
    path('delete/<int:id>' , views.delete_show , name='delete_show')
    
]