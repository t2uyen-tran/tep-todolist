from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Department(models.Model):
    departmentName = models.CharField(max_length=50, default='SOME STRING')
    departmentLocation = models.CharField(max_length=50, default='SOME STRING')
    # manage = models.OneToOneField(Employee, on_delete = models.CASCADE)

    class Meta:
        db_table = "%s" % ("Department")

    def __str__(self):
        return self.departmentName


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    # department =  models.ForeignKey(Department, on_delete = models.CASCADE, default= 1)

    class Meta:
        db_table = "%s" % ("Employee")

    # def __str__(self):
        #return self.user


class Project(models.Model):
    projectName = models.CharField(max_length=50, default='SOME STRING')
    creationDate = models.DateField()
    projectCreate = models.ForeignKey(
        Employee, on_delete=models.CASCADE, default=1, related_name='projectcreate')
    endDate = models.DateField(default="2021-10-11")
    projectDescription = models.CharField(max_length=500, default='SOME STRING')
    # department = models.ForeignKey(Department, on_delete = models.CASCADE, default= 1)
    employee = models.ManyToManyField(Employee)

    class Meta:
        db_table = "%s" % ("Project")

    def __str__(self):
        return self.projectName


class Todo(models.Model):
    # name = models.CharField(max_length=100)
    # due_date = models.DateField()

    # def __str__(self):
    #     return self.name
    taskName = models.CharField(max_length=50, default='SOME STRING')
    taskDescription = models.CharField(max_length=500, default='SOME STRING')
    taskCreate = models.ForeignKey(
        Employee, on_delete=models.CASCADE, default=1, related_name='taskcreate')
    taskDueDate = models.DateField()
    priority_choices = [
        (0, 'High'),
        (1, 'Medium'),
        (2, 'Low'),
    ]
    taskPriority = models.SmallIntegerField(
        default=0, choices=priority_choices)
    taskComplete = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "%s" % ("Todo")

    def __str__(self):
        return self.taskName
