#import all ther required modules
from fastapi import APIRouter, Depends, HTTPException, status
from ...database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession 
from ...services.book_service import BookService, BookCreate,BookUpdate
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
    return {"message":"The book created with success","data":new_book}



#get books endpoint
@router.get('/',status_code=status.HTTP_200_OK)
#method to get all books
async def get_books(skip:int = 0,limit:int = 100,book_service= Depends(get_book_service)):
    #call get all books method
    books = await book_service.get_all_books(skip,limit)

    #return the books 
    return {"message":"Success","data":books}

#get book by id
@router.get('/{id}',status_code=status.HTTP_200_OK)
#method to get book by id
async def get_books(id:int,book_service= Depends(get_book_service)):
    #call get book by id
    books = await book_service.get_book_by_id(id)

    #return the books 
    return {"message":"Success","data":books}



#get book by title
@router.get('/title/{title}',status_code=status.HTTP_200_OK)
#method to get book by title
async def get_books(title:str,book_service= Depends(get_book_service)):
    #call get book by id
    books = await book_service.get_books_by_title(title) #it can retrieve multiple books since they may share the same title

    #return the books 
    return {"message":"Success","data":books}

#update book endpoint
@router.put('/{book_id}',status_code=status.HTTP_200_OK)
#method to update the book
async def update(book:BookUpdate, book_id:int, book_service= Depends(get_book_service)):
    #Call upodate book method
    book_to_update = await book_service.update_book(book,book_id)

    return {"message":"The book has been updated with success","data":book_to_update}
