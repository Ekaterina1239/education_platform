from django.contrib.auth.models import User
from django.db import models

from courses.models import Course


class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_minutes = models.IntegerField(help_text="Duration of the test in minutes")
    max_score = models.IntegerField(help_text="Maximum achievable score")

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_completed = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'test']

    def __str__(self):
        return f"{self.user.username} - {self.test.title}: {self.score}"