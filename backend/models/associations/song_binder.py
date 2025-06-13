from sqlalchemy import Table, Column, ForeignKey
from backend.db_extension import db

song_binder_association = Table(
    "song_binder_association",
    db.metadata,
    Column("song_id", ForeignKey("songs.id"), primary_key=True),
    Column("binder_id", ForeignKey("binders.id"), primary_key=True),
)
