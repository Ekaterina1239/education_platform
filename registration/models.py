from django.contrib.auth.models import AbstractUser, User
from django.db import models


class StudentGroups(models.Model):
    title = models.CharField(max_length=255)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    appointment = models.CharField(max_length=10)


class TeacherProfile(Staff):
    bio = models.TextField()
    subjects_taught = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='teacher_profiles/', null=True, blank=True)

    def __str__(self):
        return self.user


class StudentProfile(Staff):
    group = models.ForeignKey(StudentGroups, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='student_profile/', null=True, blank=True)

