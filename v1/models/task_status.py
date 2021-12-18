from django.contrib.auth.models import User
from django.db import models
from v1.models.task import Task


class TaskStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name = "Присвоеные задачи"
        verbose_name_plural = "Присвоеные задачи"

    def __str__(self):
        return self.task.title
