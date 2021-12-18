from rest_framework import permissions
from rest_framework import viewsets
from v1.models.task_status import TaskStatus
from v1.serializers.task_status import StatusTaskSerializer


class StatusTaskViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = StatusTaskSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
