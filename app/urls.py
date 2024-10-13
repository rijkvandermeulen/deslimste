from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('quiz/<int:game_id>/<int:current_question_id>/', views.quiz_view, name='quiz'),
    path('next-question/<int:game_id>/<int:current_question_id>/', views.next_question, name='next_question'),
    path('admin/', admin.site.urls),
]
