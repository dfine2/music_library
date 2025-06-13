from typing import Any

from backend.app import app
from backend.models.entities.song import Song
from backend.db_extension import db

from backend.models.enums.genre import Genre

class SongApi:

    @staticmethod
    def create(songs: list[Song]):
        with app.app_context():
            for song in songs:
                db.session.add(song)
            db.session.commit()

    @staticmethod
    def read(song_id: str):
        with app.app_context():
            song = db.session.get(Song, song_id)
            if song:
                return song
            else:
                print("No song found.")
                return ""
            
    @staticmethod       
    def update(song_id: str, attrs: dict[str, Any]):
        with app.app_context():
            song = db.session.get(Song, song_id)
            if song:
                for key, value in attrs.items():
                    if hasattr(song, key):
                        setattr(song, key, value)
                db.session.commit()
            else:
                print("No song found.")

    @staticmethod
    def delete(song_id):
        with app.app_context():
            song = db.session.get(Song, song_id)
            if song:
                db.session.delete(song)
                print({f"Song: {song.title} deleted."})
            else:
                print("No song found.")
