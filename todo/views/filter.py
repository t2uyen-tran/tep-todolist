
""" TTUT: Views for some filtering functions
# Functions: notifications, sort, search
# Notification function:
#   - filter overdue tasks
#   - filter tasks due in 14 days
"""

import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from todo.models import Todo


@login_required
def notifications(request) -> HttpResponse:

    # to get the date that is 14 days from today
    deadline = datetime.date.today() + datetime.timedelta(days=14)

    # Filter the incomplete tasks base on logged-in user and within 14 days
    todos = Todo.objects.filter(employee=request.user).filter(taskDueDate__lte=deadline, taskComplete=False)

    context = {
        "todos": todos,
    }
    return render(request, "todo/notifications.html", context)
