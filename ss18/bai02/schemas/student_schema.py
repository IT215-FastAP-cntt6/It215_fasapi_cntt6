from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_code: str
    full_name: str
    email: str
    status: str = "ACTIVE"


class StudentResponse(BaseModel):
    id: int
    student_code: str
    full_name: str
    email: str
    status: str

    class Config:
        from_attributes = True
