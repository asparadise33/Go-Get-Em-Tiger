from django.db import models
from django.utils import timezone

class Category(models.Model):
  name_of_category = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)
