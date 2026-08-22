#import all ther required modules
from fastapi import APIRouter, Depends, HTTPException, status
from ...database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession 
from ...services.book_service import BookService, BookCreate
from ...schemas.book_schema import BookResponse
#initialize the router 
router = APIRouter(prefix="/books", tags=["Books"])

#helper function to instantiate the service with active db session
def get_book_service(db:AsyncSession = Depends(get_db)) ->BookService:
    return BookService(db)



#create post endpoint
@router.post('/',status_code=status.HTTP_201_CREATED)
 #method to create the book
async def create_book(book:BookCreate,book_service= Depends(get_book_service)):
    #call the create method from book service
    new_book = await book_service.create_book(book)
    #return the result
    return new_book





