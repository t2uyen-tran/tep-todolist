from django.conf import settings
from django.urls import path
from .views import tasks, filter


app_name = "todo"


# The `urlpatterns` list routes URLs to views.
urlpatterns = [
    path('', tasks.todo_list, name='todo_lists'),
    path('create/', tasks.todo_create),
    path('<int:id>/', tasks.todo_detail),
    path('<int:id>/update/', tasks.todo_update),
    path('<int:id>/delete/', tasks.todo_delete),
    path('mytask/', tasks.todo_mytask),
    path('notifications/', filter.notifications, name='notifications'),
    path('myproject/', tasks.todo_myproject, name='todo_myproject'),
    path('myproject/create/',
         tasks.todo_projectcreate),
]
