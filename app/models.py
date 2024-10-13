from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=10)
    picture = models.ImageField(upload_to='player_pictures/', null=True, blank=True)


class Question(models.Model):
    question = models.TextField()
    answer_1 = models.CharField(max_length=100, null=True, blank=True)
    answer_2 = models.CharField(max_length=100, null=True, blank=True)
    answer_3 = models.CharField(max_length=100, null=True, blank=True)
    answer_4 = models.CharField(max_length=100, null=True, blank=True)
    answer_5 = models.CharField(max_length=100, null=True, blank=True)


class QuestionSet(models.Model):
    questions = models.ManyToManyField(Question)


class Game(models.Model):
    name = models.CharField(max_length=100)
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_1')
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_2')
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
