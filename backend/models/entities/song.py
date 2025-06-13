from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, composite

if TYPE_CHECKING:
    from backend.models.entities.binder import Binder
from backend.models.value_objects.range import Range
from backend.models.associations.song_binder import song_binder_association
from backend.db_extension import db


class Song(db.Model):
    __tablename__ = "songs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

    album: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)
    composer: Mapped[str] = mapped_column(default="")
    character: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, default=None
    )
    genre: Mapped[Optional[str]] = mapped_column(nullable=True, default=None)
    key: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)
    original_key: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, default=None
    )
    transposed: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=0)
    lyricist: Mapped[str] = mapped_column(default="")
    range_high: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, default=None
    )
    range_low: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, default=None
    )
    range: Mapped[Range] = composite(
    Range,
    range_low, range_high
)
    s3_key: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)
    show: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)

    # Relationships (Binder and Genre must be defined elsewhere)
    binders: Mapped[Optional[list["Binder"]]] = relationship(
        "Binder", secondary=song_binder_association, back_populates="songs"
    )
    tags: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
