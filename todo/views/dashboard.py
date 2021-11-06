from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from todo.models import Todo, Project
from django.db.models import Count
import datetime


@login_required
def index(request):
    return render(request, "todo/../templates/home.html")

# Nicole

def dashboard_charts(request):
    projects = Project.objects.all()  
    project_count = Project.objects.count()
    alltodos_count = Todo.objects.count()
    todos = Todo.objects.all().order_by('project')
    deadline = datetime.date.today() + datetime.timedelta(days=14)
    todos_due = Todo.objects.filter(taskDueDate__lte=deadline, taskComplete=False).count()
    todos_overdue = Todo.objects.filter(taskDueDate__gt=deadline, taskComplete=False).count()
    todos_count = Todo.objects.values('project').annotate(dcount=Count('project'))
    emloyees = Todo.objects.all().order_by('employee')
    todos_workload = Todo.objects.values('employee').annotate(workload=Count('employee'))

    context = {
        "todoprojects": projects,
        "project_count": project_count,
        "alltodos_count": alltodos_count,
        "todos_due":todos_due,
        "todos_overdue":todos_overdue,
        "todo_list": todos,
        "task_count": todos_count,
        "employee_list": emloyees,
        "workload_count": todos_workload
    }
    return render(request, "todo/todo_dashboardcharts.html", context)

def dashboard_list(request):
    projects = Project.objects.all().order_by('endDate')
    ##todos = Todo.objects.all()
    todos = Todo.objects.all().order_by('project')
    
    context = {
        "todoprojects": projects,
        "todo_list": todos,         
    }
    return render(request, "todo/todo_dashboard.html", context)


