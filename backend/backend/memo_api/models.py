"""Models."""

from django.db import models


class Section(models.Model):
    """Section model."""

    name = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        """Converting method."""

        return f'{self.pk} @ {self.name}'


class Note(models.Model):
    """Note model."""

    name = models.CharField(max_length=300, null=False, blank=False)
    url = models.CharField(max_length=500, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    section = models.ForeignKey('Section',
                                related_name='notes',
                                on_delete=models.CASCADE)

    def __str__(self):
        """Converting method."""

        return (f'{self.pk} @ '
                f'{self.name[:10]} - '
                f'{self.url[:10]} - '
                f'{self.description[:10]} :: '
                f'{self.section}')
