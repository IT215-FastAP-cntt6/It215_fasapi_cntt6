from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Workshop(Base):
    __tablename__ = "workshops"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    maximum_participants = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default="OPEN")
    start_time = Column(DateTime, nullable=False)

    registrations = relationship("Registration", back_populates="workshop")
