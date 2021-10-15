from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('taskName', 'taskDescription', 'taskCreate',
                  'taskDueDate', 'taskPriority', 'taskComplete', 'project', 'employee')
