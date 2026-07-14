from fastapi import APIRouter, Depends
from  sqlalchemy.orm import Session
from database import get_db
import app.services.student_service as student_services

student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

#Viet API ngay ben trong router
@student_router.get("/")
def get_all_student(db: Session = Depends(get_db)):
    return {
        "message": "Lay du lieu thanh cong",
        "data": student_services.get_all_student(db)
    }