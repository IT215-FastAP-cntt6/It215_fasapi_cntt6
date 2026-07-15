from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.registration_schema import RegistrationCancel, RegistrationCreate, RegistrationResponse
from schemas.student_schema import StudentCreate, StudentResponse
from schemas.workshop_schema import WorkshopCreate, WorkshopResponse
from services.workshop_service import (
    cancel_registration,
    create_registration,
    create_student,
    create_workshop,
    get_all_students,
    get_all_workshops,
    get_student_workshops,
    get_workshop_by_id,
    get_workshop_students,
)

router = APIRouter()


@router.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student_endpoint(data: StudentCreate, db: Session = Depends(get_db)):
    return create_student(data, db)


@router.get("/students", response_model=list[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    return get_all_students(db)


@router.post("/workshops", response_model=WorkshopResponse, status_code=status.HTTP_201_CREATED)
def create_workshop_endpoint(data: WorkshopCreate, db: Session = Depends(get_db)):
    return create_workshop(data, db)


@router.get("/workshops", response_model=list[WorkshopResponse])
def list_workshops(db: Session = Depends(get_db)):
    return get_all_workshops(db)


@router.get("/workshops/{workshop_id}", response_model=WorkshopResponse)
def get_workshop_endpoint(workshop_id: int, db: Session = Depends(get_db)):
    return get_workshop_by_id(workshop_id, db)


@router.post("/registrations", response_model=RegistrationResponse, status_code=status.HTTP_201_CREATED)
def register_workshop(data: RegistrationCreate, db: Session = Depends(get_db)):
    return create_registration(data, db)


@router.get("/students/{student_id}/workshops")
def get_student_workshops_endpoint(student_id: int, db: Session = Depends(get_db)):
    return get_student_workshops(student_id, db)


@router.get("/workshops/{workshop_id}/students")
def get_workshop_students_endpoint(workshop_id: int, db: Session = Depends(get_db)):
    return get_workshop_students(workshop_id, db)


@router.put("/registrations/{registration_id}", response_model=RegistrationResponse)
def cancel_registration_endpoint(registration_id: int, db: Session = Depends(get_db)):
    return cancel_registration(registration_id, db)
