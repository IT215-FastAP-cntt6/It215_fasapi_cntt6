from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/book_db"

engine = create_engine(url=DATABASE_URL, pool_size=10)

LocalSession = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
   
