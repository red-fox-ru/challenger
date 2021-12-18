from django.db import models

from v1.models.task import Task


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    upload = models.FileField(upload_to='static/uploads/', blank=True, null=True, verbose_name='Файл')

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.upload.name
