from django.shortcuts import get_object_or_404, redirect, render

from backend.forms import SongForm
from backend.models import Song


def index(request):
    song_list = Song.objects.order_by("title")
    context = {"songs": song_list}
    return render(request, "index.html", context)


def song(request, song_id: str):
    song = get_object_or_404(Song, pk=song_id)
    context = {"song": song}
    return render(request, "song.html", context)


def new_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = SongForm()
    return render(request, "new_song.html", {"form": form})
