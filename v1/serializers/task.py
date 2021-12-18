from rest_framework import serializers
from v1.models.task import Task
from drf_writable_nested import WritableNestedModelSerializer

from v1.models.techologies import Technology


class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class TaskSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    technologies = TechnologiesSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'specialization', 'technologies', 'created_at')
