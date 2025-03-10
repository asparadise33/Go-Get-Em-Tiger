from django.db import models
from django.utils import timezone
from tigerapi.models import Habit, Category

class HabitCategory(models.Model):
  habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="habitcategory")
  category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="categoryhabit")
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)
