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
            'taskDescription': forms.Textarea(attrs={'cols': 40, 'rows': 10, 'placeholder': 'Write some descriptions about the task', 'class': 'form-control'}),
            'taskName': forms.TextInput(attrs={'size': '40', 'placeholder': 'eg. Create mysql database', 'class': 'form-control'}),
            'taskDueDate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        end_date = cleaned_data.get("taskDueDate")
        if end_date <= timezone.now().date():
            raise forms.ValidationError(
                "TaskDueDate cannot be in the past")


class TodoForm_update(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('taskName', 'taskDescription',
                  'taskDueDate', 'taskPriority', 'taskComplete', 'project', 'employee')
        widgets = {
            'taskDescription': forms.Textarea(attrs={'cols': 40, 'rows': 10, 'placeholder': 'Write some descriptions about the task', 'class': 'form-control'}),
            'taskName': forms.TextInput(attrs={'size': '40', 'placeholder': 'eg. Create mysql database', 'class': 'form-control'}),
            'taskDueDate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
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
            'projectDescription': Textarea(attrs={'cols': 40, 'rows': 10, 'class': 'form-control', 'placeholder': 'Write some descriptions about the project'}),
            'projectName': forms.TextInput(attrs={'size': '40', 'placeholder': 'eg. todolist project', 'class': 'form-control', }),
            'startDate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'endDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
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
