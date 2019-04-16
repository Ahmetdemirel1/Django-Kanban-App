from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

status = (
    ('Backlog', 'Backlog'),
    ('To do', 'To do'),
    ('In progress', 'In progress'),
    ('Done', 'Done')
)


class KanbanModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=32, choices=status, default='Backlog')