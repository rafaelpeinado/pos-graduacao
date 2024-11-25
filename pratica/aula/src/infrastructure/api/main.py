from fastapi import FastAPI
from infrastructure.api.database import create_tables
from infrastructure.api.routers import user_routers, task_routers

app = FastAPI()

app.include_router(user_routers.router)
app.include_router(task_routers.router)

create_tables()

