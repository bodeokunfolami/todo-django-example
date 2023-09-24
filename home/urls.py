from django.urls import path
from .views import home_view, create_todo_view, delete_todo_view

urlpatterns = [
  path('', home_view),
  path('create-todo/', create_todo_view),
  path('delete/<int:id>/', delete_todo_view)
]