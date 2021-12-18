from django.contrib import admin

from v1.models.attachment import Attachment
from v1.models.task import Task
from v1.models.task_status import TaskStatus
from v1.models.techologies import Technology

admin.site.register(Technology)
admin.site.register(Attachment)
admin.site.register(Task)
admin.site.register(TaskStatus)
