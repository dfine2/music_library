from rest_framework import serializers

from backend.models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"