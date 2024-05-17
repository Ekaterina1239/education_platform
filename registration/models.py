from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLES = (
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('tester', 'Tester'),
    )
    role = models.CharField(max_length=20, choices=ROLES)