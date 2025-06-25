from django.http import Http404
from django.shortcuts import render

from backend.models import Song


def index(request):
    song_list = Song.objects.order_by("title")
    context = {"songs": song_list}
    return render(request, "index.html", context)


def song(request, song_id: str):
    try:
        song = Song.objects.get(pk=song_id)
    except Song.DoesNotExist:
        raise Http404("Song does not exist.")
    context = {"song": song}
    return render(request, "song.html", context)
