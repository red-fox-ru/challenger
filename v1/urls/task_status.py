from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.views.task_status import StatusTaskViewSet

router = DefaultRouter()
router.register(r'status', StatusTaskViewSet, basename='status')
urlpatterns = [
    path(r'v1/', include(router.urls))
]
