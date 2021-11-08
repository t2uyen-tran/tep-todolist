import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static
from django.utils.translation import gettext as _

from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.conf import settings


class Department(models.Model):
    departmentName = models.CharField(max_length=50, default='SOME STRING')
    departmentLocation = models.CharField(max_length=50, default='SOME STRING')

    # manage = models.OneToOneField(Employee, on_delete = models.CASCADE)

    class Meta:
        db_table = "%s" % ("Department")

    def __str__(self):
        return self.departmentName


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

#     # department =  models.ForeignKey(Department, on_delete = models.CASCADE, default= 1)

#     class Meta:
#         db_table = "%s" % ("Employee")

#     def __str__(self):
#         return self.user.username


class Project(models.Model):
    projectName = models.CharField(max_length=50, default='')
    startDate = models.DateField()
    projectCreate = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='projectcreate')
    endDate = models.DateField(default="")
    projectDescription = models.CharField(
        max_length=500, default='')
    # department = models.ForeignKey(Department, on_delete = models.CASCADE, default= 1)
    employee = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        db_table = "%s" % ("Project")

    def __str__(self):
        return self.projectName

    def worked_by(self):
        return ", ".join([str(p) for p in self.employee.all()])


class Todo(models.Model):
    # name = models.CharField(max_length=100)
    # due_date = models.DateField()

    # def __str__(self):
    #     return self.name
    taskName = models.CharField(max_length=50, default='')
    taskDescription = models.CharField(max_length=500, default='')
    taskCreate = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='taskcreate')
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
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "%s" % ("Todo")

    def __str__(self):
        return self.taskName

    # task overdue status > return true if the task is overdue
    def is_overdue(self):
        if self.taskDueDate and datetime.date.today() > self.taskDueDate:
            return True


# Profile is an extension of the existing User model
class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_OTHER = 3
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    # default picture is used if the user does not upload a avatar
    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('img/default-profile-picture.png')


# signal to create a profile when a user is created.
@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
