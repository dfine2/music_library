from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.view_sets import SongViewSet
from . import views

router = DefaultRouter()
router.register(r"songs", SongViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]


urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
    path("songs/new/", views.new_song, name="new_song"),
    path("<int:song_id>/", views.song, name="song"),
]
