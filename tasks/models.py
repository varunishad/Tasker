from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100) #unique=True
    description = models.TextField(blank=True)
    STATUS_CHOICES = [
          ('TO_DO', 'To Do'),
          ('IN_PROGRESS', 'In Progress'),
          ('DONE', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

