from django.urls import re_path

from .views import MainView


urlpatterns = [
    # path("", MainView.as_view()),
    re_path(r'^.*$', MainView.as_view()),  # TODO: using this url make mistakes
]
