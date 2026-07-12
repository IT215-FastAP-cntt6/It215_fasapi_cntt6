from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db, Base, engine
from models import UserModel
from schema import UserRequestDTO

from user_services import create_user, get_user, update_user, delete_user


app = FastAPI(
    title="Manager Users"
)
Base.metadata.create_all(bind = engine)
@app.get("/test-connection")
def test_connections(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return{
            "message":"Kết nối thành công"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Không thể kết nối {str(e)}")

@app.post("/users", tags=["Users"], status_code=status.HTTP_201_CREATED)
def add_user(user: UserRequestDTO, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="Them du lieu khong thanh cong")
    return{
        "status_code": 201,
        "message": "Them thanh cong",
        "data": db_user
    }

@app.get("/users/{user_id}", tags=["Users"])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="ID not found")
    return{
        "status_code": 201,
        "message": "Lay du lieu thanh cong",
        "data": db_user
    }

@app.put("/users/{user_id}", tags=["Users"])
def update_user_by_id(user_id: int, user: UserRequestDTO,db: Session = Depends(get_db)):
    db_user = update_user(db, user_id,user)
    if not db_user:
        raise HTTPException(status_code=404, detail="Cap nhat khong thanh cong")
    return{
        "status_code": 201,
        "message": "cap nhat thanh cong",
        "data": db_user
    }

@app.delete("/users/{user_id}", tags=["Users"])
def delete_user_by_id(user_id: int,db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="xoa that bai")
    return{
        "status_code": 201,
        "message": "xoa thanh cong",
        "data": db_user
    }
