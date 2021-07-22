from django.urls import path, re_path

from .views import MainView


urlpatterns = [
    re_path(r'^.*$', MainView.as_view()),  # TODO: using this url make mistakes
]
