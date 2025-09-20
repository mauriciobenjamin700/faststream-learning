from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import DBConnectionManager


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    db = DBConnectionManager()
    async with db.async_session_maker() as session:
        yield session
