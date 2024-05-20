from django.db import models
from django.contrib.auth.models import User, AbstractUser

from courses.models import Lesson

# from registration.models import CustomUser





class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

