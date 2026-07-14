from sqlalchemy.orm import Session

def get_all_student(db: Session):
    return db.query()