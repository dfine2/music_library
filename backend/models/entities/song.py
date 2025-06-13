from typing import Optional, TYPE_CHECKING

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, composite

if TYPE_CHECKING:
    from backend.models.entities.binder import Binder
from backend.models.value_objects.range import Range
from backend.db_extension import db, song_binder_association


class Song(db.Model):
    __tablename__ = "songs"

    # Primary key
    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

    album: Mapped[str] = mapped_column(default="")
    composer: Mapped[str] = mapped_column(default="")
    character: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    genre: Mapped[Optional[str]] = mapped_column(nullable=True)
    key: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    lyricist: Mapped[str] = mapped_column(default="")
    range_high: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    range_low: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    range: Mapped[Range] = composite(
    Range,
    range_low, range_high
)
    s3_key: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    show: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Relationships (Binder and Genre must be defined elsewhere)
    binders: Mapped[list["Binder"]] = relationship(
        "Binder",
        secondary=song_binder_association,
        back_populates="songs", 
    )
    tags: Mapped[list[str]] = mapped_column(ARRAY(String))

