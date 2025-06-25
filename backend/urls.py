from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("songs/new/", views.new_song, name="new_song"),
    path("<int:song_id>/", views.song, name="song"),
]
