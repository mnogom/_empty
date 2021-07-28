"""Urls."""

from django.urls import path, re_path

from .views import RandomSequenceView


urlpatterns = [
    path('sequence/', RandomSequenceView.as_view()),
]
