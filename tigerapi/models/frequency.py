from django.db import models
from django.utils import timezone

class Frequency(models.Model):
  class HabitStatus(models.TextChoices):
    Scheduled ='scheduled', 'Scheduled'
    Completed = 'completed', 'Completed'
     
  habit_status = models.TextField(choices=HabitStatus.choices, default=HabitStatus.Scheduled)
  habit_occurred = models.DateTimeField(default=timezone.now)
  notes = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)
