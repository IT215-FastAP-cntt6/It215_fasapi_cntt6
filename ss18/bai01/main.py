from fastapi import FastAPI

from database import Base, engine
from models.course_model import Course
from models.enrollment_model import Enrollment
from models.student_model import Student
from routers.enrollment_router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Course Enrollment API")
app.include_router(router)
