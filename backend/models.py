import datetime
from typing import Optional

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


current_year = datetime.date.today().year
class Song(models.Model):
    title = models.CharField(max_length=60)

    album = models.CharField(max_length=100, default=None, null=True)
    artist = models.CharField(max_length=60, default=None, null=True)
    character = models.CharField(max_length=60, default=None, null=True)
    composer = models.CharField(max_length=100, default=None, null=True)
    genre = models.CharField(max_length=60, default=None, null=True)
    lyricist = models.CharField(max_length=100, default=None, null=True)
    show = models.CharField(max_length=60, default=None, null=True)
    year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(current_year)])

    def __str__(self):
        return self.title

    @property
    def decade(self) -> Optional[str]:
        if not self.year:
            return None
        decade_value = (self.year // 10) * 10
        return f"{decade_value}s"


class Arrangement(models.Model):
    name = models.CharField(max_length=100)

    key = models.CharField(max_length=10, default=None, null=True)
    original_key = models.CharField(max_length=10, default=None, null=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE,)
    transposed = models.IntegerField(default=0)
