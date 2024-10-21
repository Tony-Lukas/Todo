from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('item_main/<int:group_id>',views.item_main,name='item_main'),
    path('delete_group/<int:group_id>',views.delete_group,name='delete_group'),
    path('update_group/<int:group_id>',views.update_group, name='update_group'),

    path('add_detail/<int:pk>',views.add_detail,name='add_detail'),
    path('done_task/<int:pk>',views.done_task,name='done_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
]