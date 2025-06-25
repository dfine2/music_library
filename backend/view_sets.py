from rest_framework import viewsets

from backend.models import Song
from backend.serializers import SongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
