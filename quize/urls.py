from django.urls import path
from .views import QuizeView,RandomView

app_name = 'quize'

urlpatterns = [
    path('',QuizeView.as_view(), name="quize"),
    path('r/<str:topic>/',RandomView.as_view())
]