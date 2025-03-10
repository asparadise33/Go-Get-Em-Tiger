from django.db import models
from django.utils import timezone

class User(models.Model):
  user_name = models.TextField()
  bio = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
