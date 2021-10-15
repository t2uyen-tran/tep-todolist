from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo.forms import TodoForm, ProjectForm
from todo.models import Todo, Project
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)


@login_required
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {
        "form": form
    }
    return render(request, "todo/todo_create.html", context)


@login_required
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "todo/todo_update.html", context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")


@login_required
def todo_mytask(request):  # Tracy
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_mytask.html", context)


@login_required
def todo_myproject(request):  # Tracy
    project = Project.objects.all()
    context = {
        "project_list": project
    }
    return render(request, "todo/todo_myproject.html", context)


@login_required
def todo_projectcreate(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {
        "form": form
    }
    return render(request, "todo/todo_projectcreate.html", context)
