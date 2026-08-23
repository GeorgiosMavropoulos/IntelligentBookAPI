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


#get all author books relation endpoint
@router.get('/',status_code=status.HTTP_200_OK)
#method to get all author books relations
async def get_author_books_relationships(skip: int = 0, limit:int = 100, author_book_service=Depends(get_author_book_service)):
    #call the method from author books service to fetch all books
    author_book_relationships = await author_book_service.get_authors_books(skip,limit)

    #return the result
    return{"message":"Success","data":author_book_relationships}


#get by author author's id endpoint
@router.get('/{author_id}',status_code=status.HTTP_200_OK)
#method to fetch by author's id
async def get_author_books_relationships_by_author_id(author_id:int, author_book_service=Depends(get_author_book_service)):
    #call the method from author books service to fetch all books realtionship connected to author's id
    author_book_relationships = await author_book_service.get_by_author_id(author_id)

    #return the result
    return{"message":"Success","data":author_book_relationships}



#get by book's id endpoint
@router.get('/by_book_id/{book_id}',status_code=status.HTTP_200_OK)
#method to fetch by author's id
async def get_author_books_relationships_by_book_id(book_id:int, author_book_service=Depends(get_author_book_service)):
    #call the method from author books service to fetch all books realtionship connected to author's id
    author_book_relationships = await author_book_service.get_by_book_id(book_id)

    #return the result
    return{"message":"Success","data":author_book_relationships}


