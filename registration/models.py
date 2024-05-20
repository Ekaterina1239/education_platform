from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
# class CustomUser(AbstractUser):
#
#     ROLES = (
#         ('teacher', 'Teacher'),
#         ('admin', 'Admin'),
#         ('student', 'Student'),
#         ('tester', 'Tester'),
#     )
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',
#         blank=True,
#         verbose_name='groups',
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Specific permissions for this user.',
#     )
#     role = models.CharField(max_length=20, choices=ROLES)


class StudentGroups(models.Model):
    pass

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    subjects_taught = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='teacher_profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    group = models.ForeignKey(StudentGroups)
    profile_picture = models.ImageField(upload_to='student_profile/', null=True, blank=True)

