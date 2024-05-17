from django.db import models
from django.contrib.auth.models import User, AbstractUser

from courses.models import Lesson


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    subjects_taught = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='teacher_profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

