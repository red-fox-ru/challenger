from rest_framework import permissions
from rest_framework import viewsets
from v1.models.attachment import Attachment
from v1.serializers.attachment import AttachmentSerializer
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def pre_save(self, obj):
        obj.samplesheet = self.request.FILES.get('file')

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.AllowAny]
    #     elif self.action == 'create':
    #         permission_classes = [permissions.IsAdminUser]
    #     elif self.action == 'update':
    #         permission_classes = [permissions.IsAdminUser]
    #     elif self.action == 'destroy':
    #         permission_classes = [permissions.IsAdminUser]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]
