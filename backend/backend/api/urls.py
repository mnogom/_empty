from django.urls import path

from .views import RandomView


urlpatterns = [
    path('random/', RandomView.as_view()),
]
