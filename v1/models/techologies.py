from django.db import models


class Technology(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        verbose_name = "Технологии"
        verbose_name_plural = "Технологии"

    def __str__(self):
        return self.title
