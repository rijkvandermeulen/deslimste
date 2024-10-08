from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=10)


class Question(models.Model):
    question = models.TextField()
    answer_1 = models.CharField(max_length=100, default='Answer 1')
    answer_2 = models.CharField(max_length=100, default='Answer 2')
    answer_3 = models.CharField(max_length=100, default='Answer 3')
    answer_4 = models.CharField(max_length=100, default='Answer 4')
    answer_5 = models.CharField(max_length=100, default='Answer 5')


class QuestionSet(models.Model):
    questions = models.ManyToManyField(Question)


class Game(models.Model):
    name = models.CharField(max_length=100)
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_1')
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_2')
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
