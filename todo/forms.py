from django import forms
from .models import Todo, Project
from django.core.validators import RegexValidator
from django.forms import ModelForm, Textarea
from django.utils import timezone


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('taskName', 'taskDescription',
                  'taskDueDate', 'taskPriority', 'taskComplete', 'project', 'employee')

    # def clean_taskName(self):


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectName', 'projectCreate', 'projectDescription',
                  'creationDate', 'endDate', 'employee')
        widgets = {
            'projectDescription': Textarea(attrs={'cols': 40, 'rows': 10, 'placeholder': 'Write some descriptions about the project'}),
            'projectName': forms.TextInput(attrs={'size': '40', 'placeholder': 'eg. todolist project'}),
            'creationDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'employee': forms.CheckboxSelectMultiple(),
        }

    def clean_date1(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("creationDate")
        end_date = cleaned_data.get("endDate")
        if end_date < start_date:
            raise forms.ValidationError(
                "End date should be greater than start date.")

    def clean_date2(self):
        date = self.cleaned_data['creationDate']
        if date < timezone.now().date():
            raise forms.ValidationError("Date cannot be in the past")

    # def clean_projectName(self):
    #     projectname = self.cleaned_data["projectName"]
    #     if len(projectname) > 20:
    #         raise forms.ValidationError(
    #             'The max length of firstName is 20 characters')
    #     return projectname
