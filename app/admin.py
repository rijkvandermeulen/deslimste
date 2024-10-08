from django.contrib import admin

from app.models import Game, Player, Question, QuestionSet

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Question)
admin.site.register(QuestionSet)
