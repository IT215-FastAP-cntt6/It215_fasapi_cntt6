from fastapi import FastAPI

from database import Base, engine
from models.registration_model import Registration
from models.student_model import Student
from models.workshop_model import Workshop
from routers.workshop_router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workshop Registration API")
app.include_router(router)
