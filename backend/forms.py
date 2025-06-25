from django import forms
from backend.models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "show", "album", "composer", "lyricist", "genre", "year", "character"]