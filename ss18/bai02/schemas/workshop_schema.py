from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class WorkshopCreate(BaseModel):
    title: str
    description: Optional[str] = None
    maximum_participants: int
    status: str = "OPEN"
    start_time: datetime


class WorkshopResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    maximum_participants: int
    status: str
    start_time: datetime

    class Config:
        from_attributes = True
