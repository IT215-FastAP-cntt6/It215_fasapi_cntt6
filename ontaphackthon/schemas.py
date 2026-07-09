from pydantic import BaseModel

class BookRequesDTO(BaseModel):
    id : str
    title : str
    author : str
    isbn : str
    status  :str