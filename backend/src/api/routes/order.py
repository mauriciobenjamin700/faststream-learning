from fastapi import Depends
from faststream.rabbit.fastapi import Logger
from src.services import EventService
from src.queue import router
from src.schemas import OrderCreate, EventCreate
from sqlalchemy.ext.asyncio import AsyncSession
from src.api.dependencies import get_db_session


def validate_order(order: OrderCreate):
    return order.quantity > 0


@router.subscriber(queue="orders")
@router.publisher(queue="orders_responses")
async def process_order(
    order: OrderCreate,
    logger: Logger,
    is_valid: bool = Depends(validate_order),
    session: AsyncSession = Depends(get_db_session),
) -> dict[str, str]:
    if not is_valid:
        logger.error("Invalid order received")
        return {"detail": "Invalid order"}

    logger.info(f"Processing order for {order.quantity} of {order.product}")

    service = EventService(session)

    event = EventCreate(
        name="order_processed",
        content=order.model_dump_json()
    )

    response = await service.create_event(event)

    return {"status": "order processed", "event_id": str(response.id)}


@router.get("/ping")
async def ping():
    return {"message": "Order service online"}


@router.post("/orders")
async def create_order(order: OrderCreate):
    await router.broker.publish(order.model_dump(), "orders")
    return {"status": "pedido enviado para fila"}
