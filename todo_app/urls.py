from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('add_detail/<int:pk>',views.add_detail,name='add_detail'),
    path('done_task/<int:pk>',views.done_task,name='done_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
]