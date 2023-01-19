from django.urls import path
from .views import QuizeView,RandomView,QuestionQuize

app_name = 'quize'

urlpatterns = [
    path('',QuizeView.as_view(), name="quize"),
    path('r/<str:topic>/',RandomView.as_view()),
    path('q/<str:topic>/',QuestionQuize.as_view())
]