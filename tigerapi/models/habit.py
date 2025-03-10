from django.db import models
from django.utils import timezone
from tigerapi.models import User, Frequency, HabitTitle

class Habit(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  habititle = models.ForeignKey(HabitTitle, on_delete=models.CASCADE)
  frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE)
  notes = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)
