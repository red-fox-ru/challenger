from django.db import models
from django.utils.translation import gettext_lazy as _
from v1.models.techologies import Technology


class Task(models.Model):
    class Specializations(models.TextChoices):
        frontend = 'frontend', _('frontend')
        backend = 'backend', _('backend')
        fullstack = 'fullstack', _('fullstack')

    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    specialization = models.CharField(max_length=9, choices=Specializations.choices)
    technologies = models.ManyToManyField(Technology)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
