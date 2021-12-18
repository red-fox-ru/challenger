from rest_framework import serializers
from v1.models.task_status import TaskStatus


class StatusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('id', 'user', 'task', 'is_completed', 'started_at', 'completed_at')
