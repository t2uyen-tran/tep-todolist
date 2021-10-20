""" TTUT:
# Customise the context_processors to pass the number of tasks to Notification button on navbar
"""

import datetime
from todo.models import Todo


def add_variable_to_context(request):

    # filter the tasks that will be due in 14 days
    deadline = datetime.date.today() + datetime.timedelta(days=14)
    todos = Todo.objects.filter(employee=request.user).filter(taskDueDate__lte=deadline)

    # count the number of upcoming tasks that due in 14 days
    count = todos.count()

    return {
        'count': count
    }
