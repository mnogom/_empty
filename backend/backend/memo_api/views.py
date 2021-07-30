"""Views."""

import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .selectors import select_notes, select_sections
from .services import edit_section, create_section, delete_section, edit_note, create_note, delete_note
from .serializers import SectionSerializer, NoteSerializer
from .exceptions import MemoDataIsNotValid, MemoKeyError


def _path_endswith_digit(request):
    """Predicate to check if path ends with digit."""

    path = request.path
    path = path[:-1] if path.endswith('/') else path
    _, last_item = path.rsplit('/', 1)
    return last_item.isdigit()


def _apply_allowed_methods(rule, on_true, on_false, default=('HEAD', 'OPTIONS', 'GET', )):
    """Apply methods by rule."""

    def wrapper(fn):
        def inner(obj, request, *args, **kwargs):

            obj.allowed_methods = set(default).union(on_true if rule(request) else on_false)
            obj.headers['Allow'] = ', '.join(obj.allowed_methods)

            if request.method not in obj.allowed_methods:
                return Response({'detail': None,
                                 'message': 'method not allowed here'},
                                status=status.HTTP_405_METHOD_NOT_ALLOWED)

            return fn(obj, request, *args, **kwargs)
        return inner
    return wrapper


class SectionsView(APIView):
    """Section View."""

    allowed_methods = []


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def get(self, request, section_id=None, *args, **kwargs):
        """Get section(s)."""

        try:
            sections = select_sections(section_id=section_id)
        except MemoKeyError as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = SectionSerializer(sections, many=True)
        return Response({'detail': serializer.data,
                         'message': 'ok'},
                        status=status.HTTP_200_OK)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def post(self, request, *args, **kwargs):
        """Create section."""

        data = request.data
        try:
            section = create_section(data=data)
        except MemoDataIsNotValid as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = SectionSerializer(section)
        return Response({'detail': [serializer.data],
                         'message': 'ok'},
                        status=status.HTTP_201_CREATED)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def patch(self, request, section_id, *args, **kwargs):
        """Edit section."""

        data = request.data
        try:
            section = edit_section(section_id=section_id, data=data)
        except MemoKeyError as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_404_NOT_FOUND)
        except MemoDataIsNotValid as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = SectionSerializer(section)
        return Response({'detail': [serializer.data],
                         'message': 'ok'},
                        status=status.HTTP_200_OK)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def delete(self, request, section_id, *args, **kwargs):
        """Delete section."""

        try:
            message = delete_section(section_id=section_id)
        except MemoKeyError as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_404_NOT_FOUND)
        return Response({'detail': None,
                         'message': 'done'},
                        status=status.HTTP_200_OK)

    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def options(self, request, *args, **kwargs):
        return super().options(request, *args, **kwargs)


class NoteView(APIView):
    """ Note View."""

    allowed_methods = []


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def get(self, request, section_id, note_id=None, *args, **kwargs):
        """Get note."""

        try:
            notes = select_notes(section_id=section_id, note_id=note_id)
        except MemoKeyError as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializer(notes, many=True)
        return Response({'detial': serializer.data},
                        status=status.HTTP_200_OK)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def post(self, request, section_id, *args, **kwargs):
        """Create note."""

        data = request.data
        try:
            note = create_note(data=data, section_id=section_id)
        except MemoDataIsNotValid as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = NoteSerializer(note)
        return Response({'detail': [serializer.data],
                         'message': ''},
                        status=status.HTTP_201_CREATED)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def patch(self, request, section_id, note_id, *args, **kwargs):
        """Edit note."""

        data = request.data
        try:
            note = edit_note(section_id=section_id, note_id=note_id, data=data)
        except MemoKeyError as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_404_NOT_FOUND)
        except MemoDataIsNotValid as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = NoteSerializer(note)
        return Response({'detail': [serializer.data],
                         'message': ''},
                        status=status.HTTP_200_OK)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def delete(self, request, section_id, note_id, *args, **kwargs):
        """Delete note."""

        try:
            message = delete_note(section_id=section_id, note_id=note_id)
        except MemoKeyError as message:
            return Response({'detail': None,
                             'message': str(message)},
                            status=status.HTTP_404_NOT_FOUND)
        return Response({'detail': None,
                         'message': str(message)},
                        status=status.HTTP_200_OK)


    @_apply_allowed_methods(rule=_path_endswith_digit,
                            on_true=['PATCH', 'DELETE', ],
                            on_false=['POST', ])
    def options(self, request, *args, **kwargs):
        return super().options(request, *args, **kwargs)
