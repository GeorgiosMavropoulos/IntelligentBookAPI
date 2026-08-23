#import all ther required modules
from fastapi import APIRouter, Depends, HTTPException, status
from ...database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession 
from ...services.authors_books_service import AuthorBooks, CreateBookAuthors, AuthorsBooksService
from ...schemas.book_authors_schema import BookAuthorsResponse
#initialize the router 
router = APIRouter(prefix="/authors_books", tags=["Authors_books"])

#helper function to instantiate the service with active db session
def get_author_book_service(db:AsyncSession = Depends(get_db)) ->AuthorsBooksService:
    return AuthorsBooksService(db)



#post author books relation
@router.post('/',status_code=status.HTTP_201_CREATED)
#method to create an authors books relationship
async def create_author_book_relationship(author_book:CreateBookAuthors,author_book_service= Depends(get_author_book_service)):
    #call the method from author books service to create a relation and delegate the result into a variable
    new_author_book_relation = await author_book_service.create_author_books_relation(author_book)

    #return the result with a message of success
    return{"message":"New relation between author and book was created","data":new_author_book_relation}