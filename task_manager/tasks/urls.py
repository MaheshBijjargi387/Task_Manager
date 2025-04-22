from .views import*
from django.urls import path

urlpatterns = [
    path('',view_task,name='view_task'),
    path('create/',create_task,name='create_task'),
    path('delete/<int:id>',delete_task,name='delete'),
    path('update/<int:id>',update_task,name='update')

]
