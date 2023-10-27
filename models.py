from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from init import db

class Pet(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    spices: Mapped[str] = mapped_column(String, nullable=False)
    photo_url: Mapped[str] = mapped_column(Text)
    age: Mapped[int] = mapped_column(Integer)
    note: Mapped[str] = mapped_column(Text)
    available: Mapped[bool] = mapped_column(Boolean, nullable=False)

    def __init__(self, name, spices, photo_url, age, note, available) -> None:
        super(Pet, self).__init__()
        self.name = name
        self.spices = spices
        self.photo_url = photo_url
        self.age = age
        self.note = note
        self.available = available


