from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from todo.models import Todo, Project


@login_required
def index(request):
    return render(request, "todo/../templates/home.html")

##Nicole
def dashboard_list(request):
    projects = Project.objects.all()    
    todos = Todo.objects.all()
    context = {
        "todoprojects": projects,
        "todo_list": todos
    }
    return render(request, "todo/todo_dashboard.html", context)
