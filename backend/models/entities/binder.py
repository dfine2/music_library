from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from backend.models.entities.song import Song

from backend.db_extension import db
from backend.models.associations.song_binder import song_binder_association


class Binder(db.Model):
    __tablename__ = "binders"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    songs: Mapped[list["Song"]] = relationship(
        "Song", secondary=song_binder_association, back_populates="binders"
    )
    tags: Mapped[list[str]] = mapped_column(ARRAY(String))
