##################################################################################################
# TTUT: Views for some filtering functions                                                       #
# Functions: notifications, sort, search                                                         #
##################################################################################################
import datetime
from datetime import datetime, timedelta, timezone, time, date
from django.utils import timezone

from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Notification function:
# - Display overdue tasks
# - Display tasks due in 14 days, show in date other or priority order
# - display newly involve project (in the last 7 days)
from todo.models import Todo


@login_required
def notifications(request) -> HttpResponse:

    """deadline = datetime.date.today() + datetime.timedelta(days=14)
    today = datetime.date.today()"""

    todos = Todo.objects.filter(employee=request.user)
    """todos = Todo.objects.filter(taskDueDate__range=[today, deadline])"""

    """if deadline >= Todo.taskDueDate:
        return todos
    """
    context = {
        "todos": todos,
    }
    return render(request, "todo/notifications.html", context)
