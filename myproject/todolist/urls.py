from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_view),
    path('delete', views.delete_view),
    path('modify', views.modify_view),
    path('todo', views.todo_view),
    path('not-todo', views.not_todo_view),
    path('todo-view',views.show_view),
    path('all-delete',views.all_delete_view)
]  
