from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import order_router
from src.core import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order_router, prefix="/orders", tags=["orders"])
