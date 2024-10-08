from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('quiz/<int:game_id>/', views.quiz_view, name='quiz'),
    path('admin/', admin.site.urls),
]
