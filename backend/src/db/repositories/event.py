from sqlalchemy.ext.asyncio import AsyncSession

from src.core import BaseRepository
from src.db.models import EventModel


class EventRepository(BaseRepository[EventModel]):
    """
    Repository for EventModel with CRUD operations.

    Methods:
        - create(item: EventModel) -> EventModel
        - get(id: int) -> EventModel | None
        - list() -> list[EventModel]
        - update(item: EventModel) -> EventModel
        - delete(item: EventModel) -> None
    """

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(EventModel, session)
