from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import EventModel
from src.db.repositories import EventRepository
from src.schemas import EventCreate, EventResponse, EventUpdate


class EventService:
    """
    Service class for managing events.

    Methods:
        create_event: Create a new event.
        get_event: Retrieve an event by its ID.
        update_event: Update an existing event.
        delete_event: Delete an event by its ID.
    """
    def __init__(self, session: AsyncSession) -> None:
        self.repository = EventRepository(session)

    async def create_event(self, event_create: EventCreate) -> EventResponse:
        """
        Create a new event.
        """
        model = EventModel(**event_create.model_dump())
        created_model = await self.repository.create(model)
        return EventResponse.model_validate(created_model)

    async def get_event(self, event_id: int) -> EventResponse | None:
        """
        Retrieve an event by its ID.
        """
        model = await self.repository.get(event_id)
        if model:
            return EventResponse.model_validate(model)
        return None

    async def update_event(
        self, event_id: int, event_update: EventUpdate
    ) -> EventResponse | None:
        """
        Update an existing event.
        """
        model = await self.repository.get(event_id)
        if not model:
            return None

        update_data = event_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(model, key, value)

        updated_model = await self.repository.update(model)
        return EventResponse.model_validate(updated_model)

    async def delete_event(self, event_id: int) -> bool:
        """
        Delete an event by its ID.
        """
        model = await self.repository.get(event_id)
        if not model:
            return False
        await self.repository.delete(model)
        return True
