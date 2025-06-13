from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

song_binder_association = db.Table(
    "song_binder_association",
    db.metadata,
    db.Column("song_id", db.ForeignKey("songs.id"), primary_key=True),
    db.Column("binder_id", db.ForeignKey("binders.id"), primary_key=True),
)
