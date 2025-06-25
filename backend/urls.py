from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:song_title>/", views.song, name="song"),
]
