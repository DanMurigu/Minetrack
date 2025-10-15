from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[('dispatcher', 'Dispatcher'), ('logistics', 'Logistics'), ('production', 'Production')], blank=True, null=True)

    def __str__(self):
        return self.username