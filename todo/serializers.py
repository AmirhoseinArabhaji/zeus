from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'owner',
            'title',
            'detail',
            'is_completed',
            'due_date',
            'due_time',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'owner',
            'created_at',
            'updated_at',
        )
