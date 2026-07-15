from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RegistrationCreate(BaseModel):
    student_id: int
    workshop_id: int


class RegistrationResponse(BaseModel):
    id: int
    student_id: int
    workshop_id: int
    registered_at: datetime
    status: str

    class Config:
        from_attributes = True


class RegistrationCancel(BaseModel):
    status: str = "CANCELLED"
