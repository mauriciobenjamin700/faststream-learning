import uvicorn
from src.db import init_db


def run_server():
    # Initialize the database (create tables)
    init_db()

    # Start the FastAPI server
    uvicorn.run("src.api:app", host="0.0.0.0", port=8080)
