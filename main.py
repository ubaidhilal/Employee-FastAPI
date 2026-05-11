from fastapi import FastAPI
from core.database import Base, engine
from routes import employee

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(employee.router)
