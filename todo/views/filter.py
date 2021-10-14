##################################################################################################
# TTUT: Views for some filtering functions                                                       #
# Functions: notifications, sort, search                                                         #
##################################################################################################
import datetime

from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Notification function:
# - Display tasks due in 14 days, show in date orther or priority order
# - display newly involve project (in the last 7 days
@login_required
def notifications(request) -> HttpResponse:

    today = datetime.datetime.now()

    context = {
        "today": today,
    }
    return render(request, "todo/notifications.html", context)
