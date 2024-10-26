from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('add_group/',views.add_group,name='add_group'),
    path('delete_group/<int:group_id>',views.delete_group,name='delete_group'),
    path('update_group/<int:group_id>',views.update_group, name='update_group'),
    
    path('item_main/<int:group_id>',views.item_main,name='item_main'),
    path('add_detail/<int:pk>',views.add_detail,name='add_detail'),
    path('done_task/<int:pk>',views.done_task,name='done_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
]