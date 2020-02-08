from django.db import models
from django.utils import timezone
# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=512)
    created_time= models.DateTimeField(default=timezone.now)

