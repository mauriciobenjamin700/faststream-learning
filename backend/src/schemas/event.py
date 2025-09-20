from datetime import datetime

from src.core import BaseSchema


class EventCreate(BaseSchema):
    """
    Schema for creating an event.

    Attributes:
        name (str): The name of the event.
        content (str): The content or description of the event.
    """

    name: str
    content: str


class EventUpdate(BaseSchema):
    """
    Schema for updating an event.

    Attributes:
        name (str | None): The updated name of the event.
        content (str | None): The updated content or description of the event.
    """

    name: str | None = None
    content: str | None = None


class EventResponse(EventCreate):
    """
    Schema for responding with event details.

    Attributes:
        id (int): The unique identifier of the event.
        name (str): The name of the event.
        content (str): The content or description of the event.
        created_at (datetime): The timestamp when the event was created.
        updated_at (datetime): The timestamp when the event was last updated.
    """

    id: int
    created_at: datetime
    updated_at: datetime
