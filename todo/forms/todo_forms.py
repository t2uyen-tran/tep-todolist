from django import forms
from todo.models import Todo, Project
from django.core.validators import RegexValidator
from django.forms import ModelForm, Textarea
from django.utils import timezone
from datetime import datetime


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('taskName', 'taskDescription', 'taskCreate',
                  'taskDueDate', 'taskPriority', 'taskComplete', 'project', 'employee')
        widgets = {
            'taskDescription': Textarea(attrs={'cols': 40, 'rows': 10, 'placeholder': 'Write some descriptions about the task'}),
            'taskName': forms.TextInput(attrs={'size': '40', 'placeholder': 'eg. Create mysql database'}),
            'taskDueDate': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        end_date = cleaned_data.get("taskDueDate")
        if end_date <= timezone.now().date():
            raise forms.ValidationError(
                "TaskDueDate cannot be in the past")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectName', 'projectCreate', 'projectDescription',
                  'startDate', 'endDate', 'employee')
        widgets = {
            'projectDescription': Textarea(attrs={'cols': 40, 'rows': 10, 'placeholder': 'Write some descriptions about the project'}),
            'projectName': forms.TextInput(attrs={'size': '40', 'placeholder': 'eg. todolist project'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'employee': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startDate")
        end_date = cleaned_data.get("endDate")
        if end_date <= start_date:
            raise forms.ValidationError(
                "EndDate should be greater than startDate.")
        # if start_date < timezone.now().date():
        #     raise forms.ValidationError(
        #         "Date cannot be in the past")
