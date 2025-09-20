from types import TracebackType

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core import BaseModel, settings
from src.db.models import EventModel


class DBConnectionManager:
    """
    Connection manager for the database using SQLAlchemy's async capabilities.

    Usage:
        async with DBConnectionManager() as session:
            # Use the session for database operations
            ...
    Methods:
        - create_tables: Create all tables defined in the models.
        - drop_tables: Drop all tables defined in the models.
    """

    def __init__(self, db_url: str = settings.DB_URL) -> None:
        self.db_url = db_url
        self.session: AsyncSession | None = None
        self.__engine = create_async_engine(
            self.db_url, echo=settings.DB_ECHO
        )
        self.async_session_maker = async_sessionmaker(
            self.__engine, expire_on_commit=False
        )

    async def create_tables(self) -> None:
        async with self.__engine.begin() as conn:
            print("Creating tables...")
            await conn.run_sync(BaseModel.metadata.create_all)
            print(EventModel.metadata)
            print("Tables created successfully.")

    async def drop_tables(self) -> None:
        async with self.__engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.drop_all)

    async def __aenter__(self):
        async with self.async_session_maker() as session:
            self.session = session
            yield session

    async def __aexit__(
        self,
        exc_type: Exception,
        exc_value: Exception,
        traceback: TracebackType,
    ):
        if self.session:
            await self.session.close()
            self.session = None
