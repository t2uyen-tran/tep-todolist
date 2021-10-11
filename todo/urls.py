from django.conf import settings
from django.urls import path
from .views import tasks, dashboard

#from todo import views

#from todo.views import (todo_list, 
#                    todo_detail, 
#                   todo_create, 
#                    todo_update,
#                    todo_delete)

app_name = "todo"


# The `urlpatterns` list routes URLs to views. 
urlpatterns=[
    path('', tasks.todo_list, name='todo_lists'),
    path('create/',tasks.todo_create),
    path('<int:id>/',tasks.todo_detail),
    path('<int:id>/update/',tasks.todo_update),
    path('<int:id>/delete/',tasks.todo_delete),
    path('mytask/',tasks.todo_mytask),
]





