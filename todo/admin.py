#####################################################################################################
# TTUT:site administration use Django admin site to manage users and tasks                          #
# Description: only for internal data management (i.e. just for use by admins, or staffers          #
# Functions: to display and edit model data                                                         #
# Constraints: only "superuser" and "Staff" account can access to the admin site                    #
#####################################################################################################

from django.contrib import admin
from .models import Todo, Department, Employee, Project

# register all application models here
admin.site.register(Todo)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
