from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_view),
    path('delete/', views.delete_view),
    path('modify/', views.modify_view),
    path('todo/', views.todo_view),
    path('nottodo/', views.not_todo_view),
    path('todoview/',views.show_view),
    path('all_delete/',views.all_delete_view)
]  
