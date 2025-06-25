from django.http import HttpResponse
from django.template import loader

from backend.models import Song


def index(request):
    song_list = Song.objects.order_by("title")
    template = loader.get_template("index.html")
    context = {"songs": song_list}
    return HttpResponse(template.render(context, request))


def song(request, song_title: str):
    return HttpResponse(f"This is the page giving details for {song_title}.")
