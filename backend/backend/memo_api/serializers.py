"""Serializers."""

from rest_framework import serializers

from .models import Section, Note


class NoteSerializer(serializers.ModelSerializer):
    """Note serializer."""

    section_id = serializers.IntegerField()

    class Meta:
        """Meta class."""

        model = Note
        fields = (
            'id',
            'name',
            'url',
            'description',
            'section_id',
        )


class SectionSerializer(serializers.ModelSerializer):
    """Section serializer."""

    name = serializers.CharField(max_length=300)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        """Meta class."""

        model = Section
        fields = (
            'id',
            'name',
            'notes',
        )
