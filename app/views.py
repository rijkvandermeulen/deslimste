from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from app.models import Game, Player


def quiz_view(request, game_id, current_question_id=0):
    game = get_object_or_404(Game, id=game_id)
    current_question = game.question_set.questions.all()[current_question_id]
    context = {
        'game': game,
        'current_question': current_question,
        'current_question_id': current_question_id,
    }
    return render(request, 'app/quiz.html', context)


def next_question(request, game_id, current_question_id=0):
    # Placeholder to deduct points from player 1 and 2
    return quiz_view(request, game_id, current_question_id + 1)


def deduct_points(request, loser_id):
    player = get_object_or_404(Player, id=loser_id)
    player.points -= 10
    player.save()
    return JsonResponse({'status': 'success', 'points': player.points})
