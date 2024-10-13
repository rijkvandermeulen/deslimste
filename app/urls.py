from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.start_screen, name='start_page'),
    path('quiz/<int:game_id>/<int:current_question_id>/', views.quiz_view, name='quiz'),
    path('start_game/', views.start_game, name='start_game'),
    path('next-question/<int:game_id>/<int:current_question_id>/', views.next_question, name='next_question'),
    path('deduct_points/<int:loser_id>/', views.deduct_points, name='deduct_points'),
    path('admin/', admin.site.urls),
]
