from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.student_model import Student
from schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse
from services.enrollment_service import create_enrollment

router = APIRouter()


@router.post(
    "/enrollments",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_course(data: EnrollmentCreate, db: Session = Depends(get_db)):
    return create_enrollment(data, db)


@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    courses = []
    for enrollment in student.enrollments:
        courses.append({
            "id": enrollment.course.id,
            "name": enrollment.course.name,
        })

    return {
        "student_id": student.id,
        "full_name": student.full_name,
        "courses": courses,
    }
