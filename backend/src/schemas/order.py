from src.core import BaseSchema


class OrderCreate(BaseSchema):
    product: str
    quantity: int


class OrderResponse(OrderCreate):
    id: int
