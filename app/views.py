from django.shortcuts import render, get_object_or_404

from app.models import Game


def quiz_view(request, game_id, current_question_id=0):
    game = get_object_or_404(Game, id=game_id)
    current_question = game.question_set.questions.all()[current_question_id]
    context = {
        'game': game,
        'current_question': current_question,
        'current_question_id': current_question_id,
    }
    return render(request, 'app/quiz.html', context)
