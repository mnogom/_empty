"""Services."""

from .serializers import SectionSerializer, NoteSerializer
from .selectors import pick_section, pick_note
from .exceptions import MemoDataIsNotValid


def edit_section(section_id: int, data: dict):
    """Edit section.

    :param section_id: primal key
    :param data: data to update
    :return: updated Section
    """

    section = pick_section(section_id=section_id)
    serializer = SectionSerializer(section, data=data)
    if serializer.is_valid():
        section = serializer.save()
    else:
        raise MemoDataIsNotValid(f'Data `{data}` is not valid')
    return section


def create_section(data: dict):
    """Create section.

    :param data: data for create
    :return: created Section
    """

    serializer = SectionSerializer(data=data)
    if serializer.is_valid():
        section = serializer.save()
    else:
        raise MemoDataIsNotValid(f'Data `{data}` is not valid')
    return section


def delete_section(section_id: int):
    """Delete section.

    :param section_id: primal key
    :return: message
    """

    section = pick_section(section_id=section_id)
    section.delete()
    return 'done'


def edit_note(section_id: int, note_id: int, data: dict):
    """Edit note.

    :param section_id: primal key of section
    :param note_id: primal key if note
    :param data: data to update
    :return: updated Note
    """

    note = pick_note(section_id=section_id, note_id=note_id)
    serializer = NoteSerializer(note, data=data, partial=True)
    if serializer.is_valid():
        note = serializer.save()
    else:
        raise MemoDataIsNotValid(f'Data `{data}` is not valid')
    return note


def create_note(section_id: int, data: dict):
    """Create note.

    :param data: data for create
    :return: created Note
    """

    data['section_id'] = section_id
    serializer = NoteSerializer(data=data)

    if serializer.is_valid():
        note = serializer.save()
    else:
        raise MemoDataIsNotValid(f'Data `{data}` is not valid')
    return note


def delete_note(section_id: int, note_id: int):
    """Delete note.

    :param section_id: primal key of section id
    :param note_id: primal key of note
    :return: message
    """
    note = pick_note(section_id=section_id, note_id=note_id)
    note.delete()
    return 'done'
