from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.course_model import Course
from models.enrollment_model import Enrollment
from models.student_model import Student


def create_enrollment(data, db: Session):
    student = db.query(Student).filter(Student.id == data.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    course = db.query(Course).filter(Course.id == data.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if student.status != "ACTIVE":
        raise HTTPException(status_code=400, detail="Student is inactive")

    if course.status != "OPEN":
        raise HTTPException(status_code=400, detail="Course is closed")

    existed = db.query(Enrollment).filter(
        Enrollment.student_id == data.student_id,
        Enrollment.course_id == data.course_id,
    ).first()
    if existed:
        raise HTTPException(status_code=400, detail="Student already enrolled")

    current_students = db.query(Enrollment).filter(Enrollment.course_id == data.course_id).count()
    if current_students >= course.max_students:
        raise HTTPException(status_code=400, detail="Course is full")

    enrollment = Enrollment(student_id=data.student_id, course_id=data.course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment
