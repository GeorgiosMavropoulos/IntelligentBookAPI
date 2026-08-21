#import book model
from ..models import book_model
#import update/create from schemas
from ..schemas.book_schema import BookCreate, BookUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.database import get_db
from fastapi import HTTPException
#create book service class
class BookService:
     def __init__(self, db:AsyncSession):
        self.db = db

#create book function
async def create_book():





