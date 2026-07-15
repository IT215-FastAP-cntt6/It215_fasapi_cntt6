from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.registration_model import Registration
from models.student_model import Student
from models.workshop_model import Workshop


def create_student(data, db: Session):
    existing_student = db.query(Student).filter(Student.email == data.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already exists")

    student = Student(
        student_code=data.student_code,
        full_name=data.full_name,
        email=data.email,
        status=data.status,
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_all_students(db: Session):
    return db.query(Student).all()


def create_workshop(data, db: Session):
    workshop = Workshop(
        title=data.title,
        description=data.description,
        maximum_participants=data.maximum_participants,
        status=data.status,
        start_time=data.start_time,
    )
    db.add(workshop)
    db.commit()
    db.refresh(workshop)
    return workshop


def get_all_workshops(db: Session):
    return db.query(Workshop).all()


def get_workshop_by_id(workshop_id: int, db: Session):
    workshop = db.query(Workshop).filter(Workshop.id == workshop_id).first()
    if not workshop:
        raise HTTPException(status_code=404, detail="Workshop not found")
    return workshop


def create_registration(data, db: Session):
    student = db.query(Student).filter(Student.id == data.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    workshop = db.query(Workshop).filter(Workshop.id == data.workshop_id).first()
    if not workshop:
        raise HTTPException(status_code=404, detail="Workshop not found")

    if student.status != "ACTIVE":
        raise HTTPException(status_code=400, detail="Student is inactive")

    if workshop.status != "OPEN":
        raise HTTPException(status_code=400, detail="Workshop is closed")

    existing = db.query(Registration).filter(
        Registration.student_id == data.student_id,
        Registration.workshop_id == data.workshop_id,
        Registration.status == "ACTIVE",
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Student already registered")

    current_count = db.query(Registration).filter(
        Registration.workshop_id == data.workshop_id,
        Registration.status == "ACTIVE",
    ).count()
    if current_count >= workshop.maximum_participants:
        raise HTTPException(status_code=400, detail="Workshop is full")

    registration = Registration(student_id=data.student_id, workshop_id=data.workshop_id)
    db.add(registration)
    db.commit()
    db.refresh(registration)
    return registration


def cancel_registration(registration_id: int, db: Session):
    registration = db.query(Registration).filter(Registration.id == registration_id).first()
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")

    registration.status = "CANCELLED"
    db.commit()
    db.refresh(registration)
    return registration


def get_student_workshops(student_id: int, db: Session):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    workshops = []
    for reg in student.registrations:
        if reg.status == "ACTIVE":
            workshops.append({
                "id": reg.workshop.id,
                "title": reg.workshop.title,
                "status": reg.workshop.status,
            })
    return workshops


def get_workshop_students(workshop_id: int, db: Session):
    workshop = db.query(Workshop).filter(Workshop.id == workshop_id).first()
    if not workshop:
        raise HTTPException(status_code=404, detail="Workshop not found")

    students = []
    for reg in workshop.registrations:
        if reg.status == "ACTIVE":
            students.append({
                "id": reg.student.id,
                "full_name": reg.student.full_name,
                "email": reg.student.email,
            })
    return students
