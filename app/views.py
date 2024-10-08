from django.shortcuts import render, get_object_or_404

from app.models import Game


def quiz_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    current_question = game.question_set.questions.first()
    context = {
        'game': game,
        'current_question': current_question,
    }
    return render(request, 'app/quiz.html', context)
