from sqlalchemy import Column, String, Integer
from database import Base, engine

class BookModel(Base):
    __tablename__ ="book_managers"
    id = Column(Integer,primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    isbn = Column(String(255), unique=True)
    status = Column(String(100),nullable=False)




