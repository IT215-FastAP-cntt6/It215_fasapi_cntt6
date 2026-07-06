from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()

courses_db = [
    {
        "id": 1,
        "course_name": "FastAPI Masterclass",
        "duration_hours": 32,
        "price": 1500000,
        "status": "active",
        "created_at": "2026-07-01T02:00:00Z"
    },
    {
        "id": 2,
        "course_name": "NextJS Next-Level",
        "duration_hours": 45,
        "price": 1800000,
        "status": "active",
        "created_at": "2026-07-01T03:15:00Z"
    }
]


class CreateCourse(BaseModel):
    course_name: str = Field(..., min_length=5)
    duration_hours: int = Field(..., gt=0)
    price: int = Field(..., ge=0)


@app.get("/courses")
def get_courses():
    return {
        "statusCode": 200,
        "message": "Lấy danh sách khóa học thành công!",
        "data": courses_db,
        "error": None,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "path": "/courses"
    }


@app.post("/courses")
def create_course(course: CreateCourse):
    for item in courses_db:
        if item.get("course_name").lower() == course.course_name.lower():
            raise HTTPException(
                status_code=400,
                detail="ERR-EDU-01: Course name duplicates an existing record in memory array."
            )

    course_id = 1
    for item in courses_db:
        if course_id <= item.get("id"):
            course_id = item.get("id")

    new_course = {
        "id": course_id + 1,
        "course_name": course.course_name,
        "duration_hours": course.duration_hours,
        "price": course.price,
        "status": "active",
        "created_at": datetime.utcnow().isoformat() + "Z"
    }

    courses_db.append(new_course)

    return {
        "statusCode": 201,
        "message": "Tạo mới khóa học thành công!",
        "data": new_course,
        "error": None,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "path": "/courses"
    }


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    for course in courses_db:
        if course.get("id") == course_id:
            courses_db.remove(course)
            return {
                "statusCode": 200,
                "message": "Xóa khóa học thành công!",
                "data": None,
                "error": None,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "path": f"/courses/{course_id}"
            }

    raise HTTPException(
        status_code=404,
        detail="ERR-EDU-02: Target course ID can not be found."
    )