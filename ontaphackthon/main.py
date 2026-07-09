from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db, Base, engine
from model import BookModel

app = FastAPI(
    title="Ôn tập hackathon"
)

Base.metadata.create_all(bind=engine)

@app.get("/test_connection")
def test_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "message": "Kết nối thành công!"
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Không thể kết nối {str(e)}")