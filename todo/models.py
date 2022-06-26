from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=128)
    detail = models.CharField(max_length=2048, null=True, blank=True)

    is_completed = models.BooleanField(default=False)

    due_date = models.DateField(null=True)
    due_time = models.TimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner}: {self.title}'
