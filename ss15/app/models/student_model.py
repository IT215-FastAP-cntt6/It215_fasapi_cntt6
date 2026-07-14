from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__="students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    # Lien ket theo chieu xuoi
    profile = relationship("ProfileModel", back_populates="student", uselist=False)

# tao them bang profile
class ProfileModel(Base):
    ___tablename__="profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bio = Column(String(100), nullable=False)

    #Viet khoa ngoai 
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)

    # Lien ket theo chieu nguoc
    student = relationship("StudentModel", back_populates="profile")
# Moi quan he 1-1
