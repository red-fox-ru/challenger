from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.views import attachment

router = DefaultRouter()
router.register(r'files', attachment.AttachmentViewSet, basename='files')
urlpatterns = router.urls

# urlpatterns = [
#     path('files/', attachment.Attachment, name='files'),
# ]
