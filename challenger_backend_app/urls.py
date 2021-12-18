from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('v1.urls.task')),
    path('api/', include('v1.urls.attachment')),
    path('api/', include('v1.urls.task_status')),
    path('api/user/', include('v1.urls.auth')),
]
