from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.view_sets import SongViewSet
from . import views

router = DefaultRouter()
router.register(r"songs", SongViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
