from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
#from sqlalchemy import text 
from database import get_db, engine, Base
from app.models.student_model import StudentModel, ProfileModel
from app.routers.student_router import student_router

app = FastAPI(
    title="Get Root"
)

Base.metadata.create_all(bind = engine)

app.include_router(student_router)

@app.get("/")
def get_root():
    try:
        return"Sever dang khoi dong"
    except Exception as e:
        raise HTTPException(status_code=400, detail="Ket noi khong thanh cong!")

