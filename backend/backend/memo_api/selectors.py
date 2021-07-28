"""Selectors."""

from django.core.exceptions import ObjectDoesNotExist

from .models import Section, Note
from .exceptions import MemoKeyError


def select_sections(section_id=None):
    """Pick sections by primal key.

    :param section_id: primal key or keys
    :return: <QuerySet> of sections
    """

    sections = Section.objects
    if section_id is None:
        return sections.all().order_by('id')
    sections = sections.filter(id=section_id)
    if not sections:
        raise MemoKeyError(f'section `{section_id}` does not exists')
    return sections


def select_notes(section_id, note_id=None):
    """Pick notes by primal key.

    :param id: primal key or keys
    :return: <QuerySet> of notes
    """

    notes = Note.objects.filter(section_id=section_id)
    if note_id is None:
        return notes.all().order_by('id')
    notes = notes.filter(id=note_id)
    if not notes:
        raise MemoKeyError(f'note `{note_id}` does not exists or not in seection `{section_id}`')
    return notes


def pick_section(section_id):
    """Return single object by primal key.

    :param id: primal key
    :return: single section
    """

    try:
        return Section.objects.get(id=section_id)
    except ObjectDoesNotExist:
        raise MemoKeyError(f'section `{section_id}` does not exists')


def pick_note(section_id, note_id):
    """Return single object by primal key.

    :param id: primal key
    :return: single note"""

    try:
        note = Note.objects.get(id=note_id)
    except ObjectDoesNotExist:
        raise MemoKeyError(f'note `{note_id}` does not exists')
    if note.section_id != section_id:
        raise MemoKeyError(f'note `{note_id}` not in section {section_id}')
    return note
