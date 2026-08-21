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
     async def create_book(self, book: BookCreate):
        #try except for error handling
        try:
            book = book_model(title=book.title,
                            year=book.year,price=book.price,genre=book.genre,language=book.language, description = book.description, publisher_id=book.publisher_id,stock=book.stock)

            #add the book
            self.db.add(book)
            await self.db.commit() #commit the change in the db
            #refresh
            self.db.refresh(book)
        except: #return an error if sth goes wrong and rollbakc the action
            await self.db.rollback()
            raise




