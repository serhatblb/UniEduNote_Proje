from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # İstersen ek alan ekleyebilirsin:
    # department = models.CharField(max_length=100, blank=True, null=True)
    pass
