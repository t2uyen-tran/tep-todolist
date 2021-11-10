from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from todo.forms.todo_forms import TodoForm, TodoForm_update, ProjectForm
from todo.models import Todo, Project
from django.contrib import messages

@login_required
def todo_mytask(request):  # Tracy
    todos = Todo.objects.all()
    if not request.user.is_superuser:
        for todo in todos:
            if todo.employee_id != request.user.id:
                key = todo.id
                todos = todos.exclude(id=key)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_mytask.html", context)


@login_required  # Tracy
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)


@login_required  # Tracy
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/todo/mytask")

    context = {
        "form": form
    }
    return render(request, "todo/todo_create.html", context)


@login_required
def todo_update(request, id):  # Tracy
    todo = Todo.objects.get(id=id)
    form = TodoForm_update(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "todo/todo_update.html", context)


@login_required
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.success(request, "Task '{}' has been deleted".format(todo.taskName))
    
    return redirect("/todo/mytask")


@login_required
def todo_sortp(request):  # Tracy
    todos = Todo.objects.order_by('taskPriority')
    if not request.user.is_superuser:
        for todo in todos:
            if todo.employee_id != request.user.id:
                key = todo.id
                todos = todos.exclude(id=key)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_sortp.html", context)

@login_required
def todo_sortdate(request):  # Tracy
    todos = Todo.objects.order_by('taskDueDate')
    if not request.user.is_superuser:
        for todo in todos:
            if todo.employee_id != request.user.id:
                key = todo.id
                todos = todos.exclude(id=key)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_sortdate.html", context)



@login_required  # Tracy
def todo_search(request):
    todos = Todo.objects.all()
    query_string = request.GET.get('search')
    error_msg = ''
    found_tasks = None
    key = None
    if query_string:
        found_tasks = Todo.objects.filter(
            Q(taskName__icontains=query_string) | Q(
                taskDescription__icontains=query_string) | Q(project__projectName__icontains=query_string) | Q(
                project__projectDescription__icontains=query_string)
        )
        if not request.user.is_superuser:
            for todo in todos:
                if todo.employee_id != request.user.id:
                    key = todo.id
                    found_tasks = found_tasks.exclude(id=key)
    else:
        error_msg = 'Please enter keywords'

    

    context = {"error_msg": error_msg,
               "query_string": query_string, "found_tasks": found_tasks}
    return render(request, "todo/todo_search.html", context)


@login_required
def todo_myproject(request):
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
        return redirect("/todo/myproject/")

    context = {
        "form": form
    }
    return render(request, "todo/todo_projectcreate.html", context)

@login_required
def todo_projectupdate(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect("/todo/myproject/")
    context = {
        "form": form
    }
    return render(request, "todo/todo_projectupdate.html", context)

@login_required
def todo_projectdelete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("/todo/myproject/")


@login_required
def todo_myprojecttask(request, id):
    todos = Todo.objects.filter(project=id)
    project = Project.objects.filter(id=id)  # update:Nicole
    context = {
        "todo_list": todos,
        "project_list": project
    }
    return render(request, "todo/todo_myprojectTask.html", context)




@login_required
def todo_sortmyprojectdate(request):  # Tracy
    projects = Project.objects.order_by('endDate')
    context = {
        "project_list": projects
    }
    return render(request, "todo/todo_sortmyprojectdate.html", context)
