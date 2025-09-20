import asyncio
from src.core import settings
from .db import DBConnectionManager


async def main():
    db = DBConnectionManager(settings.DB_URL)
    await db.create_tables()


def init_db():
    asyncio.run(main())
