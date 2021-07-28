"""Urls."""

from django.urls import path, re_path

from .views import SectionsView, NoteView


urlpatterns = [
    path('sections/', SectionsView.as_view()),
    path('sections/<int:section_id>/', SectionsView.as_view()),

    path('sections/<int:section_id>/notes/', NoteView.as_view()),
    path('sections/<int:section_id>/notes/<int:note_id>/', NoteView.as_view()),

    # re_path(r'^.*$', BadRequestView.as_view()) # TODO HTTP_404_PAGE_NOT_FOUND from `api`, not `vue_app`
]
