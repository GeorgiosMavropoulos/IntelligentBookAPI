#import book model
from ..models import book_model
#import update/create from schemas
from ..schemas.book_schema import BookCreate, BookUpdate,BookResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,update
from ..database.database import get_db
from fastapi import HTTPException
from ..exceptions.book_exceptions import DuplicateISBNException,BookNotFoundException
from sqlalchemy.exc import IntegrityError
#create book service class
class BookService:
     def __init__(self, db:AsyncSession):
        self.db = db
    #create book function
     async def create_book(self, book: BookCreate):
        #try except for error handling
        try:
            #delegate into a a variable model's attributes
            book = book_model(title=book.title,
            year=book.year, isbn=book.isbn,price=book.price,genre=book.genre,language=book.language, description = book.description, publisher_id=book.publisher_id,stock=book.stock)

            #add the book
            self.db.add(book)
            await self.db.commit() #commit the change in the db
            #refresh
            await  self.db.refresh(book)
            return book #return the response

            #raise exception for duplicate isbn
        except IntegrityError as e:
            await self.db.rollback()
            raise DuplicateISBNException(book.isbn) from e
        except: #return an error if sth goes wrong and rollbakc the action
            await self.db.rollback()
            raise


     #create get all books method
     async def get_all_books(self,skip: int = 0, limit: int = 10):
       
             #create a variable to delegate to it the result
             result = await self.db.execute(select(book_model.Book).offset(skip).limit(limit))
             #return the result
             return result.scalars().all()


     #get book by id method
     async def get_book_by_id(self,book_id:int):
        
          #create a variable to delegate to it the result
          result = await self.db.execute(select(book_model.Book).where(book_model.Book.id == book_id))
          #return the result
          book = result.scalar_one_or_none()

          #return an error message if book does not exist
          if book is None:
           raise BookNotFoundException("Book does not exist")  

          #finally return the book if all goes well
          return book


    #get book by title method
     async  def get_books_by_title(self,book_title:str):
      #create a variable to delegate to it the result
      result = await self.db.execute(select(book_model.Book).where(book_model.Book.title == book_title))
      #return the result
      books = result.scalars().all()

       #return an error message if book does not exist
      if len(books) == 0:
         raise BookNotFoundException("Book does not exist")  
      
     #finally return the book if all goes well
      return books

         
     #update book method
     async def update_book(self,book:BookUpdate,book_id:int):
       #try except for error handling
       try:
           #try to retrieve the requested book
           result = await self.db.execute(select(book_model.Book).where(book_model.Book.id == book_id))


           #if all goes well delegate book's deatails into a variable
           book = result.scalar_one_or_none()

           
            #return  exception if book does not exist
           if book is None:
            raise BookNotFoundException("Book does not exist")  

           update_data = book.model_dump(exclude_unset=True) #use model dump since not all attributes should be changed

           #loop through attributes in order to change what was given
           for field, value in update_data.items():
               setattr(book, field, value)
        
           #commit
           await self.db.commit()

           #return the book
           return book
                    
       #raise exception for duplicate isbn
       except IntegrityError as e:
               await self.db.rollback()
               raise DuplicateISBNException(book.isbn) from e
       except: #return an error if sth goes wrong and rollbakc the action
               await self.db.rollback()
               raise       
         
     



