from django.db import models
from django.utils import timezone

class HabitTitle(models.Model):
  habit_name = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)
