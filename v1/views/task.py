from rest_framework import permissions
from rest_framework import viewsets
from v1.models.task import Task
from v1.serializers.task import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        elif self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]






