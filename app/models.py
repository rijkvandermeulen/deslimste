from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    # Add other player fields as needed


class Question(models.Model):
    text = models.TextField()
    # Add other question fields as needed


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)