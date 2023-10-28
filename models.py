from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from init import db

class Pet(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    species: Mapped[str] = mapped_column(String, nullable=False)
    photo_url: Mapped[str] = mapped_column(Text)
    age: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(Text)
    available: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __init__(self, **kwargs) -> None:
        super(Pet, self).__init__(**kwargs)


