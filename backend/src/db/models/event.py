from datetime import datetime

from sqlalchemy import INTEGER, TIMESTAMP, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src.core import BaseModel, constants


class EventModel(BaseModel):
    """
    Event model representing an event entity in the database.

    Attributes:
        id (int): Unique identifier for the event.
        name (str): Name of the event, cannot be null.
        content (str): Content or description of the event.
        created_at (datetime): Timestamp when the event was created.
        updated_at (datetime): Timestamp when the event was last updated.
    """

    __tablename__ = constants.EVENTS_TABLE_NAME

    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
