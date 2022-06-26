from django.urls import path, include
from rest_framework import routers

from .views import TaskModelViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskModelViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
