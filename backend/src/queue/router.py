from faststream.rabbit.fastapi import RabbitRouter
from src.core import settings

router = RabbitRouter(settings.BROKER_URL)
