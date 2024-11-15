from django.urls import path
from .views import match_view

urlpatterns = [
    path('', match_view, name='match-view'),
]