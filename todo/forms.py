from django import forms
from .models import Todo, Project


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('taskName', 'taskDescription',
                  'taskDueDate', 'taskPriority', 'taskComplete', 'project')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectName', 'projectCreate', 'projectDescription',
                  'creationDate', 'endDate', 'employee')
